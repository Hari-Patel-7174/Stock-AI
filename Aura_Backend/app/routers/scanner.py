from fastapi import APIRouter, Query
from app.services.scanner_service import bullish_breakouts, high_positive_sentiment, undervalued_quality, custom_scan

router = APIRouter()

@router.get("/scanner/bullish_breakouts")
def get_bullish_breakouts():
    return bullish_breakouts()

@router.get("/scanner/high_sentiment")
def get_high_sentiment():
    return high_positive_sentiment()

@router.get("/scanner/undervalued_quality")
def get_undervalued_quality():
    return undervalued_quality()

@router.get("/scanner/custom")
def custom_scanner(market_cap: str = Query(None), sentiment: str = Query(None), technical: str = Query(None)):
    return custom_scan(market_cap, sentiment, technical)
