from fastapi import APIRouter
from app.services.valuation_service import calculate_dcf_valuation, determine_valuation_status

router = APIRouter()

@router.get("/stock/{ticker}/valuation")
def get_valuation(ticker: str):
    # For demo, hardcoding EPS, growth, etc.
    eps = 52.0
    growth = 0.08
    discount = 0.11
    current_price = 2850.0

    fair_value = calculate_dcf_valuation(eps, growth, discount)
    status, percent_diff = determine_valuation_status(current_price, fair_value)

    return {
        "ticker": ticker,
        "fair_value": fair_value,
        "status": status,
        "percent_diff": percent_diff
    }
