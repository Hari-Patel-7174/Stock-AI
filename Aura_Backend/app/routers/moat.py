from fastapi import APIRouter
from app.services.moat_score import analyze_moat, analyze_cg

router = APIRouter()

@router.get("/stock/{ticker}/moat")
def get_moat_score(ticker: str):
    # For demo, hardcoded text input
    moat_description = "Leading player in telecom and retail"
    cg_description = "Transparent disclosures with complex structure"

    moat, moat_score = analyze_moat(moat_description)
    governance, cg_score = analyze_cg(cg_description)

    return {
        "ticker": ticker,
        "moat": moat,
        "moat_score": moat_score,
        "governance": governance,
        "cg_score": cg_score
    }
