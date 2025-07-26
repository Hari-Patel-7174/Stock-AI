from fastapi import APIRouter
from transformers import pipeline

router = APIRouter()

# Load summarization pipeline (use a lightweight summarizer for demo)
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

@router.get("/insights/summary")
def generate_insight(news: str):
    summary = summarizer(news, max_length=60, min_length=25, do_sample=False)
    return {"insight": summary[0]['summary_text']}
