import sys
import os

# Add project root to sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils.google_sheet_reader import fetch_channels_from_google_sheet
from utils.telegram_reader import extract_channel_username, fetch_latest_messages
from utils.ai_translator import translate_text_gemini
from utils.telegram_poster import send_to_telegram_channel
from utils.json_writer import save_results, load_posted_messages

import asyncio


async def main():
    telegram_api_id = os.environ['TELEGRAM_API_ID']
    telegram_api_hash = os.environ['TELEGRAM_API_HASH']
    sheet_id = os.environ['GOOGLE_SHEET_ID']
    google_sheet_api_key = os.environ['GOOGLE_SHEET_API_KEY']

    posted_messages = load_posted_messages()
    channels_data = fetch_channels_from_google_sheet(sheet_id, google_sheet_api_key)
    result_output = []

    for entry in channels_data:
        channel_username = extract_channel_username(entry["channel_link"])
        messages = await fetch_latest_messages(telegram_api_id, telegram_api_hash, channel_username)

        for msg in messages:
            if msg["text"] in posted_messages:
                print(f"⚠️ Skipping duplicate message ID {msg['id']} from {channel_username}")
                continue

            translated_text = translate_text_gemini(msg["text"])
            final_message = f"🚀 {translated_text}\n\n👉 Beli di *{entry['exchange_name']}* sini: {entry['referral_link']}"

            send_to_telegram_channel(final_message)

            result_output.append({
                "exchange_name": entry["exchange_name"],
                "channel_link": entry["channel_link"],
                "original_text": msg["text"],
                "translated_text": translated_text,
                "referral_link": entry["referral_link"],
                "date": msg["date"]
            })

    if result_output:
        save_results(result_output)

if __name__ == "__main__":
    asyncio.run(main())
