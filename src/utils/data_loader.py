"""
data_loader.py
Utility module for loading and processing market data.
"""

import random

def load_market_data(market):
    """
    Simulate loading market data for a given market.

    Args:
        market (str): The market to load data for (e.g., "ETH/USDT").

    Returns:
        dict: Simulated market data.
    """
    print(f"Loading market data for {market}...")
    
    # Simulated market data
    market_data = {
        "market": market,
        "prices": [random.uniform(1000, 2000) for _ in range(50)],
        "trend": random.choice(["bullish", "bearish", "neutral"]),
        "asset": market.split("/")[0],
    }

    print(f"Market Data: {market_data}")
    return market_data
