from fastapi import APIRouter

router = APIRouter()

# Mock Pattern Breakout Data
pattern_data = [
    {"ticker": "TCS", "pattern": "Ascending Triangle Breakout", "price": 3850},
    {"ticker": "HDFCBANK", "pattern": "Falling Wedge Breakout", "price": 1550},
]

@router.get("/patterns/breakouts")
def get_breakouts():
    return pattern_data
