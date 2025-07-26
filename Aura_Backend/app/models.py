# =================================================================
# FILE: aurafolio_backend/app/models.py (UPDATED)
# PURPOSE: To add new data structures for technical patterns.
# =================================================================

from pydantic import BaseModel, Field
from typing import List, Literal, Optional

# --- Existing Models ---

class NewsArticle(BaseModel):
    title: str = Field(..., description="The headline of the news article.")
    source: str = Field(..., description="The publisher of the news article (e.g., 'Economic Times').")
    url: str = Field(..., description="The direct URL to the full article.")
    published_at: str = Field(..., description="The publication date and time in ISO format.")
    sentiment: Literal["Positive", "Negative", "Neutral"] = Field(..., description="The AI-determined sentiment.")
    sentiment_score: float = Field(..., description="The confidence score of the sentiment prediction (0.0 to 1.0).")

class SentimentResponse(BaseModel):
    ticker: str = Field(..., description="The stock ticker symbol (e.g., 'RELIANCE').")
    overall_sentiment: Literal["Positive", "Negative", "Neutral"] = Field(..., description="The aggregated sentiment over the recent period.")
    positive_articles: int = Field(..., description="Count of recent positive articles.")
    negative_articles: int = Field(..., description="Count of recent negative articles.")
    neutral_articles: int = Field(..., description="Count of recent neutral articles.")
    articles: List[NewsArticle] = Field(..., description="A list of the most recent news articles.")

# --- NEW PATTERN MODELS ---

class DetectedPattern(BaseModel):
    """
    Represents a single technical pattern found in the price data.
    """
    name: str = Field(..., description="The name of the pattern (e.g., 'Head and Shoulders').")
    type: Literal["Bullish", "Bearish", "Neutral"] = Field(..., description="The typical implication of the pattern.")
    start_date: str = Field(..., description="The start date of the pattern formation.")
    end_date: str = Field(..., description="The end date of the pattern formation.")
    description: str = Field(..., description="A brief explanation of the pattern and its implications.")
    confidence: float = Field(..., description="A score from 0.0 to 1.0 indicating the quality of the pattern match.")

class PatternResponse(BaseModel):
    """
    The complete response for a pattern recognition request.
    """
    ticker: str = Field(..., description="The stock ticker symbol.")
    patterns_found: List[DetectedPattern] = Field(..., description="A list of technical patterns detected in the recent price history.")
