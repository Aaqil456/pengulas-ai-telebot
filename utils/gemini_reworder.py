import google.generativeai as genai

def init_gemini(api_key):
    genai.configure(api_key=api_key)
    return genai.GenerativeModel('gemini-pro')

def reword_and_translate(gemini_model, input_text):
    prompt = (
        f"Please translate and reword the following message into natural, conversational Malay "
        f"as if written by a human:\n\n\"{input_text}\""
    )
    try:
        response = gemini_model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        print(f"Gemini API error: {e}")
        return None
