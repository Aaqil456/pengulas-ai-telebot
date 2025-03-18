import os
import json
import base64
import asyncio
from utils.telegram_reader import fetch_latest_messages
from utils.gemini_reworder import init_gemini, reword_and_translate
from utils.google_sheets_reader import load_exchange_names
from utils.json_writer import save_results

# Decode Google credentials from base64 secret & save as JSON
def setup_google_credentials():
    b64_creds = os.environ['GOOGLE_CREDENTIALS_JSON_B64']
    with open('google_credentials.json', 'wb') as f:
        f.write(base64.b64decode(b64_creds))

async def main():
    setup_google_credentials()

    telegram_api_id = os.environ['TELEGRAM_API_ID']
    telegram_api_hash = os.environ['TELEGRAM_API_HASH']
    source_channel = os.environ['SOURCE_CHANNEL_USERNAME']
    gemini_api_key = os.environ['GEMINI_API_KEY']
    google_sheet_url = os.environ['GOOGLE_SHEET_URL']

    messages = await fetch_latest_messages(telegram_api_id, telegram_api_hash, source_channel)

    gemini_model = init_gemini(gemini_api_key)
    exchanges = load_exchange_names('google_credentials.json', google_sheet_url)

    results = []
    for msg in messages:
        translated_text = reword_and_translate(gemini_model, msg["text"])
        mentioned_exchanges = [ex for ex in exchanges if ex.lower() in msg["text"].lower()]
        results.append({
            "id": msg["id"],
            "original_text": msg["text"],
            "translated_text": translated_text,
            "mentioned_exchanges": mentioned_exchanges,
            "date": msg["date"]
        })

    save_results(results)

if __name__ == "__main__":
    asyncio.run(main())
