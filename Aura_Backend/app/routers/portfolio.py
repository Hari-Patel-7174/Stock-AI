from fastapi import APIRouter

router = APIRouter()

# Mock Data for Holdings & Allocation
holdings_data = [
    {"ticker": "TCS", "quantity": 50, "avg_price": 3500, "current_value": 192500, "pl_percent": 10.0},
    {"ticker": "RELIANCE", "quantity": 100, "avg_price": 2900, "current_value": 285075, "pl_percent": -1.7},
    {"ticker": "HDFCBANK", "quantity": 150, "avg_price": 1550, "current_value": 250500, "pl_percent": 8.15}
]

allocation_data = [
    {"sector": "IT & Software", "percent": 34},
    {"sector": "Banking & Finance", "percent": 25},
    {"sector": "Energy", "percent": 18},
    {"sector": "FMCG", "percent": 15},
    {"sector": "Others", "percent": 8}
]

@router.get("/portfolio/holdings")
def get_holdings():
    return holdings_data

@router.get("/portfolio/allocation")
def get_allocation():
    return allocation_data

@router.get("/portfolio/rebalance_alerts")
def get_rebalance_alerts():
    alerts = []
    for sector in allocation_data:
        if sector["percent"] > 30:
            alerts.append(f"⚠️ Sector allocation exceeded for {sector['sector']} ({sector['percent']}%)")
    return alerts
