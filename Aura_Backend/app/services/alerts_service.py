def generate_alerts(sentiment_score, valuation_status, patterns):
    alerts = []

    if sentiment_score == "Negative":
        alerts.append("⚠️ Sentiment is negative. Watch for further downside risk.")

    if valuation_status == "Overvalued":
        alerts.append("💰 Stock is overvalued. Consider reducing exposure.")

    if "RSI Overbought" in patterns:
        alerts.append("📈 RSI Overbought - potential pullback expected.")

    if "Golden Crossover" in patterns:
        alerts.append("🚀 Golden Crossover detected - potential uptrend starting.")

    return alerts

# Example usage
if __name__ == "__main__":
    alerts = generate_alerts(
        sentiment_score="Negative",
        valuation_status="Overvalued",
        patterns=["RSI Overbought"]
    )
    for alert in alerts:
        print(alert)
