# Mock Data for Scanner (In real, this comes from DB/API)
stocks_data = [
    {"ticker": "RELIANCE", "price": 2850, "resistance": 2800, "sentiment": 0.65, "moat": "Wide", "valuation": "Undervalued"},
    {"ticker": "TCS", "price": 3950, "resistance": 4000, "sentiment": 0.80, "moat": "Wide", "valuation": "Fairly Priced"},
    {"ticker": "INFY", "price": 1650, "resistance": 1600, "sentiment": 0.75, "moat": "Moderate", "valuation": "Overvalued"},
]

def bullish_breakouts():
    return [s for s in stocks_data if s["price"] > s["resistance"]]

def high_positive_sentiment():
    return [s for s in stocks_data if s["sentiment"] >= 0.70]

def undervalued_quality():
    return [s for s in stocks_data if s["moat"] == "Wide" and s["valuation"] == "Undervalued"]

def custom_scan(market_cap=None, sentiment=None, technical=None):
    # For now, simulate simple filter logic
    result = stocks_data
    if sentiment == "Positive":
        result = [s for s in result if s["sentiment"] >= 0.70]
    if technical == "Breakout":
        result = [s for s in result if s["price"] > s["resistance"]]
    return result
