import json
import os
from datetime import datetime

def save_results(messages, file_path="results.json"):
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            data = json.load(f)
            existing_messages = data.get("messages", [])
    else:
        existing_messages = []

    combined_messages = existing_messages + messages
    data = {"timestamp": datetime.now().isoformat(), "messages": combined_messages}
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)

def load_posted_messages(file_path="results.json"):
    if not os.path.exists(file_path):
        return []
    with open(file_path, "r") as f:
        data = json.load(f)
    posted_messages = [msg["original_text"] for msg in data.get("messages", [])]
    return posted_messages
