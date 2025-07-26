from fastapi import APIRouter

router = APIRouter()

@router.get("/portfolio/health_score")
def get_health_score():
    # Simple AI-driven logic (expand later with ML models)
    metrics = {
        "diversification": 80,
        "valuation_risk": 70,
        "sentiment": 75,
        "liquidity": 90
    }
    score = round(sum(metrics.values()) / len(metrics), 2)
    return {"score": score, "details": metrics}
