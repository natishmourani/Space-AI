# Space AI - Python Voice Assistant

**Space AI** is a voice-controlled AI assistant built in Python. It responds to voice commands to open websites, play music, fetch news, and chat using the **Groq API**.

---

## Features

-  Wake word detection: Activate the assistant by saying **“Space”**  
-  Open websites: Google, YouTube, Facebook, LinkedIn  
-  Play music from a predefined library  
-  Fetch latest news headlines using NewsAPI  
-  AI chat responses powered by Groq API  
-  Text-to-speech responses with `pyttsx3`  

---

## Installation & Setup

### Clone the repository

- git clone https://github.com/natishmourani/Space-AI
- cd SpaceAI

### Create a virtual environment (recommended):

- python -m venv .venv
- Activate the environment:
    - Windows: .venv\Scripts\activate
    -  Mac/Linux: source .venv/bin/activate

### Add API keys:
Create a .env file in the project folder with:
- `NEWS_API_KEY=your_newsapi_key`
- `GROQ_API_KEY=your_groq_api_key`

Make sure .env is ignored by Git (listed in .gitignore).


## Usage
- Run the assistant:
- python space_ai.py
- Say “Space” to wake it up.

- Give commands like:
  - “Open Google”
  - “Play [song name]”
  - “Give me the news”
  - Ask anything AI-related


## Project Structure
```
SpaceAI/
│── space_ai.py 
│── musicLibrary.py 
│── .env 
│── .gitignore  
```
---

## Dependencies
- Python 3.x
- speech_recognition
- pyttsx3
- requests
- groq
python-dotenv

---

## Developed By

**Natish**


