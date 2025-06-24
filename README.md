✨ Aura-Assistant
🎙️ Aura is a voice-activated personal assistant built with Python. It can open websites, play Nasheed's, fetch the latest news, answer questions using AI, and much more — just say “Aura”!

---

✨ Features

- 🧠 **Ask AI Anything** – Uses OpenRouter (Mistral 7B) to answer general knowledge questions
- 🎵 **Play Nasheeds** – Say “play Ummati” and it plays from YouTube
- 📰 **Get News** – Reads top 3 headlines using NewsAPI
- 🌐 **Open Websites** – Opens Google, YouTube, Facebook, LinkedIn
- 🔍 **Search the Web** – Say “search about planets” to open Google Search
- 🕒 **Tells Current Time** – Just say “what time is it?”
- 🎤 **Voice Activated** – Only responds after you say “Aura”
- 🪵 **Logs Commands** – Saves command history in a log file

---

🛠️ Tech Stack

- Python 3.12
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
- [gTTS (Google Text-to-Speech)](https://pypi.org/project/gTTS/)
- [pygame](https://pypi.org/project/pygame/) – for audio playback
- [pyttsx3](https://pypi.org/project/pyttsx3/) – fallback voice system
- [OpenRouter.ai](https://openrouter.ai/) – for AI responses (Mistral 7B)
- [NewsAPI](https://newsapi.org/) – for latest headlines

---

📂 Project Structure
Aura/
├── main.py # Main assistant logic
├── client.py # Connects to OpenRouter AI
├── nasheedLibrary.py # Nasheed links library
├── .env # Stores your API key (not shared)
├── requirements.txt # List of dependencies
└── aura_log.txt # Command logs (auto-generated)

---

🚀 Getting Started

 1. Clone the repository
```bash
git clone https://github.com/UnaizaAsif/Aura-Assistant.git
cd Aura-Assistant
```

2. Create virtual environment (optional but recommended)
```bash
python -m venv .venv
.venv\Scripts\activate   # On Windows
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Add your API keys
Create a file called `.env` in the root folder with this content:
```env
OPENROUTER_API_KEY=your_openrouter_api_key_here
```
You can get a free OpenRouter key from https://openrouter.ai
(Optional) Sign up at https://newsapi.org and use your NewsAPI key in `main.py`:
```python
newsapi = "your_news_api_key"
```

5. Run the assistant
```bash
python main.py
```

---

🗣️ Sample Commands

> Say **"Aura"** first to activate, then:

| Command                     | What Happens                             |
|----------------------------|------------------------------------------|
| “What is force?”           | Uses AI to answer                       |
| “Play Ummati”              | Plays the nasheed from YouTube          |
| “Tell me the news”         | Speaks top 3 headlines                  |
| “What time is it?”         | Tells current time                      |
| “Open Google”              | Opens Google in browser                 |
| “Search about black holes” | Opens Google Search for black holes     |

---

✅ Requirements

Install using:
```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install SpeechRecognition gTTS pygame pyttsx3 requests python-dotenv
```

---

💡 Tip: Running Issues?

- ✅ Make sure your mic is working
- ✅ Run from terminal inside VS Code
- ✅ If `gTTS` fails, long responses fall back to `pyttsx3`
- ✅ If `PyAudio` fails, install it with:
  ```
  pip install pipwin
  pipwin install pyaudio
  ```

---

GitHub: [github.com/UnaizaAsif](https://github.com/UnaizaAsif)



