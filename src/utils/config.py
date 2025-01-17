"""
config.py
Utility module for loading and managing configuration files.
"""

import json

def load_config(config_path):
    """
    Load configuration from a JSON file.

    Args:
        config_path (str): Path to the configuration file.

    Returns:
        dict: Configuration data.
    """
    print(f"Loading configuration from {config_path}...")
    try:
        with open(config_path, "r") as file:
            config = json.load(file)
            print("Configuration successfully loaded.")
            return config
    except FileNotFoundError:
        print(f"Error: Configuration file not found at {config_path}")
        raise
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in {config_path}")
        raise
