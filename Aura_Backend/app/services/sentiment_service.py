# =================================================================
# FILE: aurafolio_backend/app/services/sentiment_service.py (FINAL UPGRADE)
# PURPOSE: To fetch LIVE news and analyze it with our REAL AI model.
# =================================================================

# Import necessary libraries and modules
from app.models import SentimentResponse, NewsArticle
from datetime import datetime, timedelta
from transformers import pipeline
import requests  # For making HTTP requests to the News API
import os        # To access environment variables
from dotenv import load_dotenv # To load variables from our .env file
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# --- CONFIGURATION & INITIALIZATION ---

# Load environment variables from the .env file
load_dotenv()

# Load the News API key from the environment.
# The application will stop if this key is not found.
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
if not NEWS_API_KEY:
    raise ValueError("NEWS_API_KEY not found in environment variables. Please create a .env file.")

# Initialize the AI model pipeline (this happens only once on startup)
print("INFO: Initializing AI Sentiment Analysis pipeline...")
sentiment_pipeline = pipeline("sentiment-analysis", model="ProsusAI/finbert")
print("INFO: AI Pipeline initialized successfully.")


def get_sentiment_for_ticker(ticker: str) -> SentimentResponse:
    """
    This function performs the full, end-to-end sentiment analysis process:
    1. Fetches live news articles from the NewsAPI.org service.
    2. Runs each article's title through the FinBERT AI model.
    3. Aggregates the results into a comprehensive response.
    """
    print(f"INFO: Starting LIVE sentiment analysis for ticker: {ticker}")

    # --- 1. FETCH LIVE NEWS ---
    
    # We look for news from the last 7 days.
    date_from = (datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d')
    
    # This is the URL for the NewsAPI endpoint.
    # We search for the ticker name and filter for English language news.
    news_url = (f"https://newsapi.org/v2/everything?"
                f"q={ticker}&"
                f"from={date_from}&"
                f"sortBy=relevancy&"
                f"language=en&"
                f"apiKey={NEWS_API_KEY}")

    try:
        # Make the actual request to the News API
        response = requests.get(news_url)
        # Raise an exception if the request was not successful (e.g., 4xx or 5xx errors)
        response.raise_for_status()
        news_data = response.json()
    except requests.exceptions.RequestException as e:
        print(f"ERROR: Could not fetch news from NewsAPI: {e}")
        # In a real app, you might want to return a more specific error message.
        # For now, we return None to indicate failure.
        return None

    # --- 2. ANALYZE NEWS WITH AI ---
    
    analyzed_articles = []
    positive_count = 0
    negative_count = 0
    neutral_count = 0
    
    # Check if the API returned any articles
    if news_data.get("status") == "ok" and news_data.get("articles"):
        # We'll analyze up to the first 20 articles to keep it fast
        for article_data in news_data["articles"][:20]:
            title = article_data.get("title")
            if not title:
                continue

            # Run the AI model on the headline
            result = sentiment_pipeline(title)[0]
            sentiment_label = result['label'].capitalize()

            # Count the results
            if sentiment_label == "Positive": positive_count += 1
            elif sentiment_label == "Negative": negative_count += 1
            else: neutral_count += 1

            # Create our NewsArticle object
            article = NewsArticle(
                title=title,
                source=article_data.get("source", {}).get("name", "Unknown"),
                url=article_data.get("url"),
                published_at=article_data.get("publishedAt"),
                sentiment=sentiment_label,
                sentiment_score=round(result['score'], 4)
            )
            analyzed_articles.append(article)
    else:
        print(f"WARN: No articles found for ticker {ticker} from NewsAPI.")
        # If no articles are found, we can return an empty but valid response
        return SentimentResponse(
            ticker=ticker.upper(),
            overall_sentiment="Neutral",
            positive_articles=0, negative_articles=0, neutral_articles=0,
            articles=[]
        )


    # --- 3. AGGREGATE AND RETURN RESPONSE ---

    # Determine overall sentiment
    if positive_count > negative_count: overall = "Positive"
    elif negative_count > positive_count: overall = "Negative"
    else: overall = "Neutral"

    # Create and return the final response object
    return SentimentResponse(
        ticker=ticker.upper(),
        overall_sentiment=overall,
        positive_articles=positive_count,
        negative_articles=negative_count,
        neutral_articles=neutral_count,
        articles=analyzed_articles
    )