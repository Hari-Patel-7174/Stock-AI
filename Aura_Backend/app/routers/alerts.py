from fastapi import APIRouter
from app.services.alerts_service import generate_alerts

router = APIRouter()

@router.get("/stock/{ticker}/alerts")
def get_alerts(ticker: str):
    # Example static inputs
    sentiment_score = "Negative"
    valuation_status = "Overvalued"
    patterns = ["RSI Overbought"]

    alerts = generate_alerts(sentiment_score, valuation_status, patterns)

    return {
        "ticker": ticker,
        "alerts": alerts
    }
