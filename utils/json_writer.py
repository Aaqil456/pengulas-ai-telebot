import json
from datetime import datetime

def save_results(messages, file_path="results.json"):
    data = {
        "timestamp": datetime.now().isoformat(),
        "messages": messages
    }
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)
