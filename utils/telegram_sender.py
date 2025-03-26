import requests
import html
import os

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_telegram_message_html(translated_text, exchange_name=None, referral_link=None):
    # Escape special characters for safe HTML display
    safe_text = html.escape(translated_text).replace('\n', '<br>')

    message_html = ""
    if exchange_name:
        message_html += f"<b>{exchange_name}</b> just posted an update:<br><br>{safe_text}"
    else:
        message_html += f"{safe_text}"

    if referral_link:
        message_html += f"<br><br>👉 <a href='{referral_link}'>Register & Trade here</a>"

    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message_html,
        "parse_mode": "HTML",
        "disable_web_page_preview": False
    }

    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print(f"✅ Telegram message sent successfully.")
        else:
            print(f"❌ Telegram send error: {response.text}")
    except Exception as e:
        print(f"❌ Telegram send exception: {e}")
