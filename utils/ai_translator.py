import requests
import os
import time

GEMINI_API_KEY = os.environ['GEMINI_API_KEY']

def translate_text_gemini(text):
    if not text or not isinstance(text, str) or not text.strip():
        return "Translation failed"

    retries = 3
    for attempt in range(retries):
        try:
            gemini_url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"
            headers = {"Content-Type": "application/json"}
            payload = {
                "contents": [
                    {"parts": [
                        {"text": f"Translate this text '{text}' into Malay. Only return the translated text without any explanation. Use natural, conversational, friendly Malaysian Malay — like how a friend shares info. Keep it simple, relaxed, and easy to understand. Avoid using exaggerated slang words or interjections (such as "Eh," "Korang," "Woi," "Wooohooo," "Wooo," or anything similar). No shouting words or unnecessary excitement. Keep it informative, approachable, and casual — but clean and neutral. Do not use emojis unless they appear in the original text. Do not translate brand names or product names."}
                    ]}
                ]
            }
            response = requests.post(gemini_url, headers=headers, json=payload)
            response.raise_for_status()

            data = response.json()
            translated_text = data["candidates"][0]["content"]["parts"][0]["text"]

            if translated_text.strip():
                return translated_text.strip()
            else:
                print(f"[Warning] Empty translation result for: {text}")
        except Exception as e:
            print(f"[Error] Translation attempt {attempt+1} failed: {e}")
            time.sleep(2)  # wait before retry

    return "Belum ada akaun exchange kripto ?"
