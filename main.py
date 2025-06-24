import speech_recognition as sr
import webbrowser
import pyttsx3
import nasheedLibrary as musicLibrary
import requests
from client import ask_ai
from gtts import gTTS
import pygame
import os
import uuid
from datetime import datetime
from difflib import get_close_matches

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "3c4725e536b94ec6b7d5dd3a1cb1baf9"

def speak(text):
    filename = f"{uuid.uuid4()}.mp3"
    tts = gTTS(text)
    tts.save(filename)
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.music.unload()
    os.remove(filename)

def processCommand(c):
    c = c.lower()
    
    # Log command
    with open("aura_log.txt", "a") as log:
        log.write(f"{datetime.now()}: Command: {c}\n")

    if "open google" in c:
        webbrowser.open("https://google.com")
    elif "open facebook" in c:
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c:
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c:
        webbrowser.open("https://linkedin.com")
    elif c.startswith("play"):
        song = c.replace("play", "").strip().lower()
        matches = get_close_matches(song, musicLibrary.Nash.keys(), n=1)
        if matches:
            webbrowser.open(musicLibrary.Nash[matches[0]])
        else:
            speak("I couldn't find that nasheed.")
            
    elif "news" in c:
        print("Fetching news...")
        try:
            r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
            print("Status Code:", r.status_code)
            if r.status_code == 200:
                articles = r.json().get('articles', [])
                print("Found", len(articles), "articles")
                for article in articles[:3]:
                    print("Title:", article['title'])
                    speak(article['title'])
            else:
                print("Bad response from NewsAPI:", r.text)
                speak("Sorry, I couldn't fetch the news right now.")
        except Exception as e:
            print("News error:", e)
            speak("There was an issue connecting to the news service.")

    elif "time" in c:
        now = datetime.now().strftime('%I:%M %p')
        speak(f"The current time is {now}")
    elif "search" in c and "about" in c:
        topic = c.split("about")[-1].strip().replace(" ", "+")
        url = f"https://www.google.com/search?q={topic}"
        speak(f"Searching for {topic.replace('+', ' ')}")
        webbrowser.open(url)
    else:
        output = ask_ai(c)
        speak(output)

if __name__ == "__main__":
    speak("Initializing Aura....")
    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                try:
                    audio = recognizer.listen(source, timeout=3, phrase_time_limit=3)
                except sr.WaitTimeoutError:
                    continue
            word = recognizer.recognize_google(audio)
            if word.lower() == "aura":
                speak("Yes?")
                with sr.Microphone() as source:
                    print("Aura Active... Listening for command")
                    try:
                        audio = recognizer.listen(source, timeout=5)
                    except sr.WaitTimeoutError:
                        speak("I didn't hear anything.")
                        continue
                try:
                    command = recognizer.recognize_google(audio)
                    print(f"You said: {command}")
                    processCommand(command)
                except sr.UnknownValueError:
                    speak("Sorry, I couldn't understand that.")
        except Exception as e:
            print("Error:", e)
