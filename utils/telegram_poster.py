import requests
import os

def send_to_telegram_channel(message):
    bot_token = os.environ['TELEGRAM_BOT_TOKEN']
    chat_id = os.environ['TELEGRAM_CHAT_ID']

    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {"chat_id": chat_id, "text": message, "parse_mode": "Markdown"}

    response = requests.post(url, json=payload)
    if response.status_code == 200:
        print("✅ Message sent to Telegram channel.")
    else:
        print(f"❌ Telegram send error: {response.text}")

