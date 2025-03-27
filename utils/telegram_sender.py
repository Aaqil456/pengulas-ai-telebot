import requests
import html
import os

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_telegram_message_html(translated_text, exchange_name=None, referral_link=None):
    safe_text = html.escape(translated_text)

    message_html = f"{safe_text}"
    if referral_link:
        message_html += f"\n\n👉 <a href=\"{referral_link}\">Daftar di {exchange_name}</a>"

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
            print("✅ Telegram message sent successfully (HTML mode).")
        else:
            print(f"❌ Telegram send error: {response.text}")
    except Exception as e:
        print(f"❌ Telegram send exception: {e}")

def send_photo_to_telegram_channel(image_path, translated_caption, exchange_name=None, referral_link=None):
    # Build full caption
    safe_caption = html.escape(translated_caption)

    if referral_link:
        safe_caption += f"\n\n👉 <a href=\"{referral_link}\">Daftar di {exchange_name}</a>"

    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendPhoto"
    with open(image_path, "rb") as photo_file:
        payload = {
            "chat_id": TELEGRAM_CHAT_ID,
            "caption": safe_caption,
            "parse_mode": "HTML"
        }
        files = {"photo": photo_file}
        response = requests.post(url, data=payload, files=files)

    if response.status_code == 200:
        print("✅ Photo + caption sent successfully.")
    else:
        print(f"❌ Failed to send photo: {response.text}")
