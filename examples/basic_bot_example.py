"""
basic_bot_example.py
Example implementation of a simple trading bot using AI TradeBot Maker.
"""

from src.agents.trade_bot import TradeBot

def main():
    # Path to the bot configuration file
    config_path = "configs/bot_config.json"

    # Initialize and run the trading bot
    print("Starting the basic trading bot...")
    bot = TradeBot(config_path)
    bot.run()

if __name__ == "__main__":
    main()
