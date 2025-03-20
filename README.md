# 📊 Exchange Info AI Agent

A fully automated AI agent that:
- Fetches the latest messages from multiple Telegram channels (exchange news).
- Translates and rewords the messages into **Malay** using Google Gemini AI.
- Compares exchange names from the message against your Google Sheet.
- If matched, adds the correct referral link from the Google Sheet.
- Posts the translated and customized message into your Telegram channel.
- Logs everything into a `results.json` file for audit and duplicate prevention.

---

## ✅ Key Features
- Automatic reading of multiple Telegram channel messages.
- Secure Telegram authentication using an encrypted `.session` file.
- Fully integrated Google Sheets API connection for referral matching.
- AI-powered translation and rewording using Gemini AI.
- Automated posting to Telegram via bot.
- Runs automatically via GitHub Actions.

---

## ✅ Project Structure

```
exchange-info-ai-agent/
│
├─ exchange_info_ai_agent.py           # Main execution script
├─ utils/
│   ├─ __init__.py
│   ├─ telegram_reader.py              # Reads Telegram messages using Telethon
│   ├─ google_sheet_reader.py          # Reads exchange and channel data from Google Sheet
│   ├─ translator.py                   # Handles translation and rewording using Gemini AI
│   └─ telegram_sender.py              # Posts messages to your Telegram channel
│
├─ results.json                        # Output log file (auto-generated)
├─ requirements.txt                    # Python dependencies
├─ init_session.py                     # Script to generate Telegram .session file (one-time setup)
└─ .github/workflows/main.yml          # GitHub Actions workflow automation
```

---

## ✅ Setup Guide (Step-by-step)

### 1️⃣ Generate Telegram Session
- Run `init_session.py` locally:
```bash
python init_session.py
```
- Provide your `TELEGRAM_API_ID` and `TELEGRAM_API_HASH`.
- Enter your phone number, verification code, and 2FA (if required).
- After success, you'll get `telegram_session.session`.

### 2️⃣ Convert the Session File to Base64
```bash
base64 telegram_session.session > session_base64.txt
```
- Open `session_base64.txt` and copy the entire content.

### 3️⃣ Add Secrets to GitHub Repository
Go to **GitHub > Settings > Secrets > Actions** and add these secrets:

| Secret Name               | Value                                               |
|---------------------------|-----------------------------------------------------|
| `TELEGRAM_SESSION_B64`    | (paste base64 content from `session_base64.txt`)    |
| `TELEGRAM_API_ID`         | Your Telegram API ID                               |
| `TELEGRAM_API_HASH`       | Your Telegram API HASH                             |
| `TELEGRAM_BOT_TOKEN`      | Your Telegram Bot token (for posting)              |
| `TELEGRAM_CHAT_ID`        | Your Telegram Channel ID                           |
| `GOOGLE_SHEET_ID`         | Your Google Sheet ID                              |
| `GOOGLE_SHEET_API_KEY`    | Google API Key to access the sheet                |
| `GEMINI_API_KEY`          | Google Gemini AI API Key                          |
| `ACTIONS_PAT`             | Your GitHub Personal Access Token (for auto push) |

### 4️⃣ Google Sheet Structure Example
| Name    | Category | Link                                                    | TelegramChannelLink                      |
|---------|----------|---------------------------------------------------------|------------------------------------------|
| Bybit   | CEX      | https://partner.bybitglobal.com/b/bicarakrypto          | https://t.me/Bybit_Official             |
| MEXC    | CEX      | https://www.mexc.co/register?inviteCode=mexc-bicarak   | https://t.me/MEXCofficialNews           |
| Binance | CEX      | https://www.binance.info/activity/referral-entry/CPA...| https://t.me/binance_announcements      |

---

## ✅ Workflow Overview
- GitHub Actions runs on schedule or manual dispatch.
- Decodes the `.session` file from `TELEGRAM_SESSION_B64` secret.
- Fetches Telegram channel messages.
- Translates to Malay and rewords using Gemini AI.
- Checks against exchanges in Google Sheet.
- Adds referral link if matched.
- Posts to your Telegram channel.
- Logs everything in `results.json`.

---

## ✅ Common Errors & Fixes
| Error                                                        | Cause & Solution                                                                                        |
|--------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| `can't parse entities` Telegram error                        | Happens due to broken Markdown. Fix: escape special characters or switch to HTML parse mode.            |
| `ValueError: 'TelegramChannelLink' is not in list`           | Google Sheet header mismatch. Make sure header exactly matches `TelegramChannelLink`.                   |
| `EOFError: EOF when reading a line` on GitHub Actions run    | You attempted to generate `.session` in a non-interactive environment. Only generate `.session` locally.|

---

## ✅ Recommendations
- Keep your repo **public** but never commit the `.session` file.
- Store all sensitive items in GitHub Secrets.
- Regularly rotate your session if security changes.
- If frequent markdown issues occur, consider switching to HTML parse mode.

---

## ✅ Credits
Built by: [Your Name]

---

> Enjoy automated affiliate marketing with AI-powered translation & referral linking!

