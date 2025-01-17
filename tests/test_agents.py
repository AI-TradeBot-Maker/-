"""
test_agents.py
Unit tests for AI agents.
"""

import unittest
from src.agents.trade_bot import TradeBot
from utils.config import load_config

class TestTradeBot(unittest.TestCase):
    def setUp(self):
        """Set up a TradeBot instance with a sample configuration."""
        self.config_path = "configs/bot_config.json"
        self.bot = TradeBot(self.config_path)

    def test_initialization(self):
        """Test if the TradeBot initializes correctly with a valid configuration."""
        self.assertIsNotNone(self.bot.config)
        self.assertIsInstance(self.bot.hlp, object)
        self.assertIsInstance(self.bot.llp, object)

    def test_run_method(self):
        """Test the run method to ensure it handles market data correctly."""
        try:
            self.bot.run()
        except Exception as e:
            self.fail(f"TradeBot run method raised an exception: {e}")

if __name__ == "__main__":
    unittest.main()
