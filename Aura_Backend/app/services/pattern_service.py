# =================================================================
# FILE: aurafolio_backend/app/services/pattern_service.py (NEW FILE)
# PURPOSE: Contains the logic for identifying technical patterns in price data.
# =================================================================

import pandas as pd
import numpy as np
from scipy.signal import find_peaks
from app.models import PatternResponse, DetectedPattern
from datetime import datetime, timedelta

def find_patterns_for_ticker(ticker: str) -> PatternResponse:
    """
    This function simulates fetching price data and identifying patterns.
    
    In the future, this will:
    1. Fetch historical price data from a service like Alpha Vantage or a broker API.
    2. Run a series of algorithms to detect various patterns.

    For now, it uses a pre-defined mock dataset to demonstrate the logic for
    finding a "Head and Shoulders" pattern.
    """
    print(f"INFO: Running pattern recognition for ticker: {ticker}")

    # --- MOCK PRICE DATA (to be replaced with a live API call) ---
    # This data is crafted to represent a classic "Head and Shoulders" pattern.
    # A real implementation would fetch ~200 days of data.
    dates = pd.to_datetime([datetime.now() - timedelta(days=x) for x in range(100, 0, -1)])
    prices = [
        100, 102, 105, 108, 110, # Left shoulder rise
        112, 115, 113, 111, 109, # Left shoulder peak and fall
        105, 107, 104, 106, 103, # Neckline
        108, 112, 116, 120, 124, # Head rise
        128, 130, 127, 125, 120, # Head peak and fall
        115, 110, 106, 104, 102, # Neckline
        107, 110, 114, 116, 118, # Right shoulder rise
        119, 117, 115, 112, 110, # Right shoulder peak and fall
        108, 105, 103, 100, 98, 95 # Breakdown
    ]
    # Ensure prices list has the same length as dates
    prices = prices + [95] * (len(dates) - len(prices))
    
    price_data = pd.DataFrame({'date': dates, 'price': prices})
    price_data.set_index('date', inplace=True)

    # --- PATTERN RECOGNITION LOGIC ---
    
    patterns_found = []
    
    # Simple algorithm to find a Head and Shoulders pattern
    # 1. Find all peaks in the price data
    # The 'prominence' helps filter out minor peaks.
    peaks, _ = find_peaks(price_data['price'], prominence=5)

    if len(peaks) >= 3:
        # Sort peaks by height (price)
        sorted_peaks = sorted(peaks, key=lambda p: price_data['price'].iloc[p], reverse=True)
        
        head_idx = sorted_peaks[0]
        
        # Find two other peaks that are lower than the head
        shoulders = [p for p in sorted_peaks[1:3]]
        
        if len(shoulders) == 2:
            # Check if the head is between the shoulders chronologically
            left_shoulder_idx = min(shoulders, key=lambda p: price_data.index[p])
            right_shoulder_idx = max(shoulders, key=lambda p: price_data.index[p])

            if left_shoulder_idx < head_idx < right_shoulder_idx:
                pattern = DetectedPattern(
                    name="Head and Shoulders",
                    type="Bearish",
                    start_date=price_data.index[left_shoulder_idx].strftime('%Y-%m-%d'),
                    end_date=price_data.index[right_shoulder_idx].strftime('%Y-%m-%d'),
                    description="A bearish reversal pattern that can signal the end of an uptrend. It consists of three peaks, with the central peak (the head) being the highest.",
                    confidence=0.85 # Confidence is high as our mock data is perfect
                )
                patterns_found.append(pattern)

    # You would add more `if` blocks here to check for other patterns like
    # "Double Top", "Double Bottom", "Triangles", etc.

    return PatternResponse(ticker=ticker.upper(), patterns_found=patterns_found)
