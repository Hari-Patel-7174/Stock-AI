from fastapi import APIRouter, HTTPException

router = APIRouter()

# Mock user database
users_db = {
    "hari@example.com": {"password": "aurafolio123", "watchlist": ["TCS", "RELIANCE"]}
}

@router.post("/auth/login")
def login(email: str, password: str):
    user = users_db.get(email)
    if not user or user["password"] != password:
        raise HTTPException(status_code=401, detail="Invalid Credentials")
    return {"message": "Login successful", "watchlist": user["watchlist"]}

@router.post("/watchlist/add")
def add_to_watchlist(email: str, ticker: str):
    if email not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    users_db[email]["watchlist"].append(ticker)
    return {"message": f"{ticker} added to watchlist", "watchlist": users_db[email]["watchlist"]}

@router.get("/watchlist/get")
def get_watchlist(email: str):
    if email not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    return {"watchlist": users_db[email]["watchlist"]}
