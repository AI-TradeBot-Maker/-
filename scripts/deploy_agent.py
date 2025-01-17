"""
deploy_agent.py
Script to deploy an AI trading agent using AI TradeBot Maker.
"""

from src.agents.trade_bot import TradeBot

def deploy():
    """
    Deploy the trading agent with the specified configuration.
    """
    print("Deploying AI trading agent...")
    
    # Path to the bot configuration file
    config_path = "configs/bot_config.json"

    # Initialize and deploy the trading bot
    bot = TradeBot(config_path)
    bot.run()

if __name__ == "__main__":
    deploy()
