import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import datetime
import os
import requests
from bs4 import BeautifulSoup


assistant = pyttsx3.init('sapi5')
voices = assistant.getProperty('voices')
assistant.setProperty('voice',voices[2].id)

def speak(audio):
    print(audio)
    assistant.say(audio)
    assistant.runAndWait()
speak("नमस्कार गुरु जी माई आपकी किस तरह मदद कर स्कति हूं")
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 1
        r.energy_threshold = 500
        audio = r.listen(source)
    try:
        print("Recognizing......")
        querry = r.recognize_google(audio,language='en-in')
        print(f"You said: {querry}\n")
    except Exception as E:
        print("Phir se bolo..")
        return "None"
    return querry
while True:
    querry = takeCommand().lower()
    if "wikipedia" in querry:
        speak('Searching from Wikipedia Pleas wait')
        querry = querry.replace("wikipedia","")
        results = wikipedia.summary(querry,sentences=2)
        speak('According to wikipedia')
        speak(results)
    elif "youtube" in querry:
        webbrowser.open("youtube.com")
    elif "facebook" in querry:
        webbrowser.open("facebook.com")
    elif "time" in querry:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The Time Is {strTime}")
    elif "file manager" in querry:
        path = "E:\\digha"
        os.startfile(path)
    elif "who" in querry:
        queue = querry.replace("google search","")
        url = f"https://www.google.com/search?q={queue}"
        headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}
        page = requests.get(url,headers=headers)
        soup = BeautifulSoup(page.content,'html.parser')
        result = soup.find(class_='kno-rdesc').get_text()
        speak(result)

    elif "whether" or "temperature" in querry:
        queue = querry
        lst = queue.split(" ")
        url = f"https://www.google.com/search?q={queue}"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}
        page = requests.get(url, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        result = soup.find(class_='wob_t q8U8x').text
        speak("Current temperature is {result} degree celcius hai")