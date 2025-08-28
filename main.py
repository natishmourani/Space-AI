import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests 
import time
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

recognizer = sr.Recognizer()
engine = pyttsx3.init()

newsApi = os.getenv("NEWS_API_KEY")
groq_api_key = os.getenv("GROQ_API_KEY")

def groq_ai(command):
    client = Groq(api_key = groq_api_key)

    chat_completion = client.chat.completions.create(
        model="llama3-8b-8192",   
        messages=[
            {"role": "system", "content": "You are a helpful AI assistant named Space. Give short responces"},
            {"role": "user", "content": command}
        ]
    )

    return chat_completion.choices[0].message.content

voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)  
engine.setProperty("rate", 170)           
engine.setProperty("volume", 1.0)   


def processCommand(c):
    print(f"You: {command}")
    if "open google" in c.lower():
        webbrowser.open("https://google.com")        
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")        
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")        
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")       
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.songs[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsApi}")
        if r.status_code == 200: 
            data = r.json() 
            articles = data.get("articles", [])
            
            print("Top Headlines:\n")
            for i, article in enumerate(articles, start=1):
                print(f"{i}. {article['title']}")
                pyttsx3.speak(article['title'])

    else: 
        output = groq_ai(c)
        print(output)
        pyttsx3.speak(output)


if __name__ == "__main__":
    pyttsx3.speak("Initializing space...")

    while True : 
        #Listen for wake word
        r = sr.Recognizer()
        print("Recognizing....")
        
        try: 
            with sr.Microphone() as source:
                print("Listening....")
                audio = r.listen(source, timeout=5, phrase_time_limit=3)

            word = r.recognize_google(audio)
            if "space" in word.lower():
                print("wake word detected!")
                pyttsx3.speak("yaa")

                with sr.Microphone() as source:
                    print("Space Active....")
                    audio = r.listen(source, timeout=5, phrase_time_limit=3)
                    command = r.recognize_google(audio)
                    processCommand(command)

        except Exception as e:
            print(f"Error: {e}") 

