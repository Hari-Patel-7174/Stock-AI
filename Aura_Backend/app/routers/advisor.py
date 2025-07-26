from fastapi import APIRouter

router = APIRouter()

@router.get("/advisor/ask")
def portfolio_advice(query: str):
    # Mock intelligent responses for demo
    if "rebalance" in query.lower():
        return {"response": "You should consider reducing IT sector exposure by 4% to stay within your target allocation."}
    elif "tcs outlook" in query.lower():
        return {"response": "TCS shows bullish sentiment due to recent contract wins. Short-term outlook is positive."}
    else:
        return {"response": "I need more context to give specific advice. Please provide a detailed query."}
