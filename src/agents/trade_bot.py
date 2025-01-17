"""
trade_bot.py
Core script for running an AI-powered trading bot.
"""

import json
import time
from sdk.hlp import HighLevelPlanner
from sdk.llp import LowLevelPlanner
from utils.data_loader import load_market_data
from utils.config import load_config

class TradeBot:
    def __init__(self, config_path):
        # Load configuration
        self.config = load_config(config_path)
        self.hlp = HighLevelPlanner(self.config)
        self.llp = LowLevelPlanner(self.config)

    def run(self):
        """Main loop for the trading bot."""
        print("Starting TradeBot...")
        while True:
            try:
                # Load market data
                market_data = load_market_data(self.config["market"])
                
                # Generate a high-level plan
                strategy = self.hlp.generate_plan(market_data)
                
                # Execute the strategy
                self.llp.execute_strategy(strategy)
                
                # Wait before the next iteration
                time.sleep(self.config["trade_interval"])
            
            except Exception as e:
                print(f"Error encountered: {e}")
                break

if __name__ == "__main__":
    # Specify configuration file
    CONFIG_PATH = "configs/bot_config.json"

    # Initialize and run the bot
    bot = TradeBot(CONFIG_PATH)
    bot.run()
