"""
strategy.py
Module for defining trading strategies used by the TradeBot.
"""

class Strategy:
    def __init__(self, config):
        self.config = config

    def generate(self, market_data):
        """
        Generate a trading strategy based on market data.

        Args:
            market_data (dict): Real-time market data.

        Returns:
            dict: A strategy plan containing actions and parameters.
        """
        print("Generating strategy...")
        strategy = {}

        # Example: Simple Moving Average (SMA) strategy
        prices = market_data["prices"]
        short_window = self.config["short_window"]
        long_window = self.config["long_window"]

        if len(prices) >= long_window:
            short_sma = sum(prices[-short_window:]) / short_window
            long_sma = sum(prices[-long_window:]) / long_window

            if short_sma > long_sma:
                strategy["action"] = "buy"
                strategy["amount"] = self.config["trade_amount"]
            elif short_sma < long_sma:
                strategy["action"] = "sell"
                strategy["amount"] = self.config["trade_amount"]
            else:
                strategy["action"] = "hold"

        return strategy
