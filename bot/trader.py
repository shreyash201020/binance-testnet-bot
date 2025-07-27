# bot/trader.py

from binance.client import Client
from dotenv import load_dotenv
import os

def start_bot():
    print("🚀 Bot is starting...")

    load_dotenv()

    api_key = os.getenv("API_KEY")
    api_secret = os.getenv("API_SECRET")

    print("🔑 API_KEY:", api_key)
    print("🔐 API_SECRET:", api_secret)

    if not api_key or not api_secret:
        print("❌ API keys not loaded properly from .env file.")
        return

    client = Client(api_key, api_secret)
    client.API_URL = 'https://testnet.binance.vision/api'

    try:
        account_info = client.get_account()
        print("✅ Connected to Binance Testnet!")
        print("📄 Account Info:")
        print(account_info)
    except Exception as e:
        print("❌ Failed to connect:", str(e))
