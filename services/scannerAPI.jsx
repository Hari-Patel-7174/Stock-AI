export async function getHighSentimentStocks() {
    const response = await fetch('http://127.0.0.1:8000/api/scanner/high_sentiment');
    return await response.json();
}
