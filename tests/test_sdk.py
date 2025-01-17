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
        marke
