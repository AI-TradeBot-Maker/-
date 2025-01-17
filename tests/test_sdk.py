"""
test_sdk.py
Unit tests for GAME SDK components (HLP and LLP).
"""

import unittest
from src.sdk.hlp import HighLevelPlanner
from src.sdk.llp import LowLevelPlanner

class TestHighLevelPlanner(unittest.TestCase):
    def setUp(self):
        """Set up a HighLevelPlanner instance with a sample configuration."""
        self.config = {"trade_amount": 100}
        self.hlp = HighLevelPlanner(self.config)

    def test_generate_plan_bullish(self):
        """Test plan generation for bullish market conditions."""
        market_data = {"trend": "bullish", "asset": "ETH"}
        plan = self.hlp.generate_plan(market_data)
        self.assertEqual(plan["action"], "buy")
        self.assertEqual(plan["asset"], "ETH")
        self.assertEqual(plan["amount"], 100)

    def test_generate_plan_bearish(self):
        """Test plan generation for bearish market conditions."""
        market_data = {"trend": "bearish", "asset": "BTC"}
        plan = self.hlp.generate_plan(market_data)
        self.assertEqual(plan["action"], "sell")
        self.assertEqual(plan["asset"], "BTC")
        self.assertEqual(plan["amount"], 100)

    def test_generate_plan_neutral(self):
        """Test plan generation for neutral market conditions."""
        market_data = {"trend": "neutral", "asset": "USDT"}
        plan = self.hlp.generate_plan(market_data)
        self.assertEqual(plan["action"], "hold")

class TestLowLevelPlanner(unittest.TestCase):
    def setUp(self):
        """Set up a LowLevelPlanner instance with a sample configuration."""
        self.config = {}
        self.llp = LowLevelPlanner(self.config)

    def test_execute_buy(self):
        """Test execution of a buy action."""
        strategy = {"action": "buy", "asset": "ETH", "amount": 1}
        self.llp.execute_strategy(strategy)

    def test_execute_sell(self):
        """Test execution of a sell action."""
        strategy = {"action": "sell", "asset": "BTC", "amount": 1}
        self.llp.execute_strategy(strategy)

    def test_execute_hold(self):
        """Test execution of a hold action."""
        strategy = {"action": "hold"}
        self.llp.execute_strategy(strategy)

if __name__ == "__main__":
    unittest.main()
