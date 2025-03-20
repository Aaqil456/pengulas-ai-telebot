from telethon import TelegramClient

def extract_channel_username(url):
    return '@' + url.strip().rstrip('/').split('/')[-1]

async def fetch_latest_messages(api_id, api_hash, channel_username, limit=5):
    client = TelegramClient("telegram_session", api_id, api_hash)
    await client.start()
    messages = []

    async for message in client.iter_messages(channel_username, limit=limit):
        if message.text:
            messages.append({
                "id": message.id,
                "text": message.text,
                "date": str(message.date)
            })

    await client.disconnect()
    return messages
