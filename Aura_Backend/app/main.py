# =================================================================
# FILE: aurafolio_backend/app/main.py (UPDATED)
# PURPOSE: To add the new API endpoint for pattern recognition.
# =================================================================

from fastapi import FastAPI, HTTPException
# Import the new models and service
from app.models import SentimentResponse, PatternResponse
from app.services.sentiment_service import get_sentiment_for_ticker
from app.services.pattern_service import find_patterns_for_ticker
from fastapi import FastAPI
from app.routers import valuation, moat, alerts
from app.routers import scanner, valuation, moat
from app.routers import scanner  # Import scanner router
from app.routers import scanner, valuation, moat, alerts  # Import routers
from app.routers import portfolio
from app.routers import insights
from app.routers import patterns
from app.routers import advisor
from app.routers import newsfeed
from app.routers import health
from app.routers import auth

app = FastAPI()
app.include_router(auth.router, prefix="/api")
app.include_router(health.router, prefix="/api")
app.include_router(newsfeed.router, prefix="/api")
app.include_router(advisor.router, prefix="/api")
app.include_router(patterns.router, prefix="/api")
app.include_router(insights.router, prefix="/api")
app.include_router(portfolio.router, prefix="/api")
app.include_router(scanner.router, prefix="/api")  # Add to FastAPI
app.include_router(valuation.router, prefix="/api")
app.include_router(moat.router, prefix="/api")
app.include_router(alerts.router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "AuraFolio Backend API is running!"}


app = FastAPI(
    title="AuraFolio API",
    description="The backend engine for the AuraFolio intelligent investment co-pilot.",
    version="0.2.0" # Version bump!
)

# --- Existing Endpoints ---

@app.get("/")
def read_root():
    return {"message": "Welcome to the AuraFolio Backend. The AI engine is running."}

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/api/v1/stock/{ticker}/sentiment", response_model=SentimentResponse)
def get_stock_sentiment(ticker: str):
    if not ticker.isalpha() or len(ticker) > 10:
        raise HTTPException(status_code=400, detail="Invalid ticker format.")
    sentiment_data = get_sentiment_for_ticker(ticker)
    if not sentiment_data:
        raise HTTPException(status_code=404, detail=f"No sentiment data found for ticker: {ticker}")
    return sentiment_data

# --- NEW PATTERN ENDPOINT ---

@app.get("/api/v1/stock/{ticker}/patterns", response_model=PatternResponse)
def get_stock_patterns(ticker: str):
    """
    This endpoint analyzes historical price data for a given stock ticker
    and identifies classic technical analysis patterns.
    """
    if not ticker.isalpha() or len(ticker) > 10:
        raise HTTPException(status_code=400, detail="Invalid ticker format.")
        
    # Call the service function to get the pattern data
    pattern_data = find_patterns_for_ticker(ticker)
    
    if not pattern_data:
        raise HTTPException(status_code=404, detail=f"Could not analyze patterns for ticker: {ticker}")
        
    return pattern_data