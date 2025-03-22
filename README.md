# 🎙️ Rio- Virtual AI Assistant 🤖

RIO is a **Python-based virtual assistant** that can perform various tasks like opening applications, searching Wikipedia, playing music, sending emails, telling jokes, and more.

---

## 📌 Features
- ✅ **Voice Commands**: Responds to user voice inputs.
- ✅ **Time & Date**: Tells the current time and date.
- ✅ **Wikipedia Search**: Fetches information from Wikipedia.
- ✅ **Email Sending**: Sends emails via Gmail.
- ✅ **Web Browsing**: Opens websites and searches Google/YouTube.
- ✅ **System Monitoring**: Checks CPU usage and battery status.
- ✅ **News Updates**: Fetches top headlines.
- ✅ **Jokes**: Tells jokes using the `pyjokes` library.
- ✅ **Screenshots**: Captures and saves screenshots.
- ✅ **Music Player**: Plays music from a local directory.
- ✅ **Application Control**: Opens and closes applications like Notepad, Chrome, Paint, etc.
- ✅ **Shutdown & Restart**: Controls system power options.

---
##Dependencies
Python libraries:

pyttsx3 - Text-to-speech conversion

speech_recognition - Recognizing voice commands

wikipedia - Fetching information from Wikipedia

smtplib - Sending emails via SMTP

webbrowser - Opening web pages

psutil - System monitoring (CPU & battery)

pyjokes - Fetching random jokes

pyautogui - Automating keyboard & mouse tasks

requests & json - Fetching data from APIs

wolframalpha - Answering computational queries

pywhatkit - YouTube & WhatsApp automation

##🎯 How It Works
The assistant listens to your voice through a microphone.

It recognizes your command using speech_recognition.

Based on the command, it performs an action, such as:

Telling the time (time_())

Searching Wikipedia (wikipedia.summary())

Opening applications (os.startfile())

Fetching news (requests.get())

Telling a joke (pyjokes.get_joke())

Taking a screenshot (pyautogui.screenshot())
##Future Improvements
🌟 Add support for more voice commands.

🌟 Integrate ChatGPT API for better responses.

🌟 Improve GUI using Tkinter or PyQt.

🌟 Add WhatsApp & Email Automation.



