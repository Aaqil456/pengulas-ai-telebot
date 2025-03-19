import requests
import os

GEMINI_API_KEY = os.environ['GEMINI_API_KEY']

def translate_text_gemini(text):
    if not text or not isinstance(text, str) or not text.strip():
        return "Translation failed"

    gemini_url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"
    headers = {"Content-Type": "application/json"}
    payload = {
        "contents": [
            {
                "parts": [
                    {
                        "text": f"Translate this text '{text}' into Malay. Only return the translated text, structured like an article. Please exclude or don't take any sentences that looks like an advertisement from the text."
                    }
                ]
            }
        ]
    }

    try:
        response = requests.post(gemini_url, json=payload, headers=headers)
        response.raise_for_status()
        gemini_response = response.json()
        translated_text = gemini_response.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text")
        return translated_text.strip() if translated_text else "Translation failed"
    except Exception as e:
        print(f"Gemini API error: {e}")
        return "Translation failed"
