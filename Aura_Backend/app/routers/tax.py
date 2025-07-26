from fastapi import APIRouter

router = APIRouter()

holdings_data = [
    {"ticker": "TCS", "buy_price": 3500, "current_price": 3850, "quantity": 50},
    {"ticker": "INFY", "buy_price": 1600, "current_price": 1480, "quantity": 100},
    {"ticker": "RELIANCE", "buy_price": 2900, "current_price": 2850, "quantity": 80},
]

@router.get("/tax/harvest_opportunities")
def tax_harvest():
    opportunities = []
    for stock in holdings_data:
        pl_percent = ((stock["current_price"] - stock["buy_price"]) / stock["buy_price"]) * 100
        if pl_percent < 0:
            loss_amount = (stock["buy_price"] - stock["current_price"]) * stock["quantity"]
            opportunities.append({
                "ticker": stock["ticker"],
                "loss": round(loss_amount, 2),
                "suggestion": f"Consider harvesting ₹{loss_amount:.2f} loss to offset capital gains."
            })
    return opportunities
