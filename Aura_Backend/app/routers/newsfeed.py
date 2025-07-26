from fastapi import APIRouter
import requests

router = APIRouter()

NEWS_API_KEY = "YOUR_NEWSAPI_KEY"

@router.get("/newsfeed/latest")
def get_latest_news(ticker: str):
    url = f"https://newsapi.org/v2/everything?q={ticker}&sortBy=publishedAt&apiKey={NEWS_API_KEY}"
    response = requests.get(url)
    articles = response.json().get("articles", [])[:5]  # Top 5 latest news
    news_list = [{"title": a["title"], "url": a["url"]} for a in articles]
    return news_list
