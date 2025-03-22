import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import psutil
import pyjokes
import os
import pyautogui
import random
import requests
import json
from urllib.request import urlopen
import wolframalpha
import time

# Initialize the speech engine
engine = pyttsx3.init()
wolframalpha_app_id = 'your_wolframalpha_id_here'

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def get_time():
    return datetime.datetime.now().strftime("%H:%M:%S")

def get_date():
    now = datetime.datetime.now()
    return now.day, now.month, now.year

def greetings():
    hour = datetime.datetime.now().hour
    if 6 <= hour < 12:
        speak('Good morning sir')
    elif 12 <= hour < 18:
        speak('Good afternoon sir')
    elif 18 <= hour < 24:
        speak('Good evening sir')
    else:
        speak('Good night sir')
    speak('I am at your service. How can I help you today?')

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 0.7
        r.adjust_for_ambient_noise(source)  # Adjusts for ambient noise
        audio = r.listen(source)
        
        try:
            print('Recognizing...')
            query = r.recognize_google(audio, language='en-US')
            print(f"You said: {query}")
            return query.lower()
        except sr.UnknownValueError:
            print('Could not understand audio. Please say again.')
            return None
        except sr.RequestError as e:
            print(f'Error with the speech recognition service; {e}')
            return None

def send_email(to, content):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)  # Use the correct SMTP server and port
        server.starttls()
        server.login('your_email@gmail.com', 'your_password')  # Replace with your email and password
        server.sendmail('your_email@gmail.com', to, content)  # Replace with your email
        server.close()
        speak('Email has been sent.')
    except Exception as e:
        print(f'Error sending email: {e}')
        speak("I'm sorry, I couldn't send the email.")

def cpu_status():
    usage = psutil.cpu_percent()
    battery = psutil.sensors_battery().percent
    speak(f'CPU usage is at {usage}%')
    speak(f'Battery percentage is at {battery}%')
    print(f'CPU usage: {usage}%')
    print(f'Battery: {battery}%')

def tell_joke():
    joke = pyjokes.get_joke()
    speak(joke)
    print(joke)

def take_screenshot():
    img = pyautogui.screenshot()
    img.save("screenshot.png")
    speak('Screenshot taken and saved.')

def get_top_headlines():
    try:
        api_key = 'your_api_key_here'
        url = f'https://newsapi.org/v2/top-headlines?country=us&category=entertainment&apiKey={api_key}'
        response = urlopen(url)
        data = json.load(response)

        if 'articles' in data:
            print('===========TOP HEADLINES==========')
            for i, article in enumerate(data['articles'], start=1):
                title = article.get('title', 'No title available')
                description = article.get('description', 'No description available')

                print(f'{i}. {title}\n{description}\n')
                speak(title)

    except Exception as e:
        print(f'Error fetching headlines: {e}')

def handle_query(query):
    if 'time' in query:
        speak(f'The current time is {get_time()}')
    elif 'date' in query:
        day, month, year = get_date()
        speak(f'Today is {day} {month} {year}')
    elif 'wikipedia' in query:
        speak("Searching Wikipedia...")
        query = query.replace('wikipedia', '')
        result = wikipedia.summary(query, sentences=3)
        speak(f'According to Wikipedia: {result}')
    elif 'send email' in query:
        speak("What should I say?")
        content = take_command()
        speak("Who is the receiver?")
        receiver = input('Enter receiver email: ')
        send_email(receiver, content)
    elif 'open chrome' in query:
        speak("What should I search?")
        search = take_command().lower()
        wb.open(f'https://www.google.com/search?q={search}')
    elif 'search on youtube' in query:
        query = query.replace('search on youtube', '')
        wb.open(f'https://www.youtube.com/results?search_query={query}')
    elif 'close browser' in query:
        os.system("taskkill /f /im chrome.exe")
    elif 'news' in query:
        get_top_headlines()
    elif 'cpu' in query or 'battery' in query:
        cpu_status()
    elif 'joke' in query:
        tell_joke()
    elif 'screenshot' in query:
        take_screenshot()
    elif 'play music' in query:
        music_dir = "E:/my_music"  # Update with your music directory
        songs = os.listdir(music_dir)
        os.startfile(os.path.join(music_dir, random.choice(songs)))
    elif 'offline' in query:
        speak('Thank you sir, I am going offline.')
        exit()

if __name__ == '__main__':
    greetings()
    while True:
        command = take_command()
        if command:
            handle_query(command)
