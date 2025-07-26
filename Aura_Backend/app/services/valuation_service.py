def calculate_dcf_valuation(eps, growth_rate, discount_rate, years=5):
    """
    Calculates DCF fair value per share using future projected EPS and discounting.
    """
    projected_eps = [eps * ((1 + growth_rate) ** i) for i in range(1, years + 1)]
    discounted_eps = [eps / ((1 + discount_rate) ** i) for i, eps in enumerate(projected_eps, 1)]
    fair_value = sum(discounted_eps)
    return round(fair_value, 2)

def determine_valuation_status(current_price, fair_value):
    diff = (fair_value - current_price) / current_price
    if diff > 0.1:
        return "Undervalued", round(diff * 100, 2)
    elif diff < -0.1:
        return "Overvalued", round(diff * 100, 2)
    else:
        return "Fairly Priced", round(diff * 100, 2)

if __name__ == "__main__":
    eps = 52.0  # example earnings per share
    growth = 0.08  # 8% growth
    discount = 0.11  # 11% discount rate
    price = 2850

    fair_val = calculate_dcf_valuation(eps, growth, discount)
    status, percent = determine_valuation_status(price, fair_val)

    print(f"Fair Value: ₹{fair_val}")
    print(f"Valuation Status: {status} ({percent}%)")
