"""
test_utils.py
Unit tests for utility modules.
"""

import unittest
from src.utils.data_loader import load_market_data
from src.utils.config import load_config

class TestDataLoader(unittest.TestCase):
    def test_load_market_data(self):
        """Test if market data is loaded and contains expected keys."""
        market = "ETH/USDT"
        market_data = load_market_data(market)
        self.assertIn("market", market_data)
        self.assertIn("prices", market_data)
        self.assertIn("trend", market_data)
        self.assertIn("asset", market_data)
        self.assertEqual(market_data["market"], market)

class TestConfigLoader(unittest.TestCase):
    def test_load_config_valid(self):
        """Test loading a valid configuration file."""
        config_path = "configs/bot_config.json"
        config = load_config(config_path)
        self.assertIsInstance(config, dict)
        self.assertIn("trade_interval", config)

    def test_load_config_invalid_path(self):
        """Test handling of a non-existent configuration file."""
        with self.assertRaises(FileNotFoundError):
            load_config("invalid_path.json")

    def test_load_config_invalid_format(self):
        """Test handling of an invalid JSON format in a config file."""
        with self.assertRaises(Exception):
            load_config("configs/invalid_config.json")

if __name__ == "__main__":
    unittest.main()
