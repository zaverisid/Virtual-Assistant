import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import wolframalpha
import webbrowser
import os
import sys
import random
import smtplib
import cv2
import tkinter as tk
import pywhatkit
import pyjokes
from requests import get

MASTER = 'Sid'

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

client = wolframalpha.Client('K6Y537-G9KHELRWVH')


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    speak("Hello, This is Jarvis. I am your virtual assistant")
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning!" + MASTER)

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!" + MASTER)

    else:
        speak("Good Evening!" + MASTER)

    speak("How may i help You?")



def takeCommand():
    # it takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 2 #press ctrl on pause threshhold to increse decrese sensitivity 
        audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User Said: {query}\n")

        except Exception as e:
            e = "I didnt quite get you, Please Say that again"
            speak(e)
            print("Say That Again Please....")
            return "None"

        return query


if __name__ == "__main__":
    wishMe()
    while True:
        # if 1:
        query = takeCommand().lower()
        # logic for executing task based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            url = "youtube.com"
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)

        elif 'open google' in query:
            url = "google.com"
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)
            speak("Sir, what should i search on google?")
            cm = takeCommand().lower()
            webbrowser.open(f"you searched {cm}")

        elif 'open instagram' in query:
            url = "instagram.com"
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)

        elif 'open linkedin' in query:
            url = "linkedin.com"
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)

        elif 'open facebook' in query:
            url = "facebook.com"
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)

        elif 'open stack overflow' in query:
            url = "stackoverflow.com"
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)

        elif 'open command prompt' in query:
            os.system('start cmd')
            
        elif 'open camera' in query:
            speak("Press Q to exit")
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                if cv2.waitKey(10) == ord('q'):
                    break
            cap.release()
            cv2.destroyAllWindows()
            

        elif 'ip address' in query:
            ip = get('https://api.ipify.org').text
            speak(f"your IP Address is {ip}")

        elif 'send message' in query:
            pywhatkit.sendwhatmsg('+919833398555', 'i love you', 14, 12)

            

        elif 'play' in query:
            song = query.replace('play', '')
            speak('playing' + song)
            pywhatkit.playonyt(song)

              # elif 'play music' in query:
        #     music_dir = 'C:\\Users\\siddhant\\Downloads\\music'
        #     songs = os.listdir(music_dir)
        #     print(songs)
        #     os.startfile(os.path.join(music_dir, songs[0]))

        # elif 'play perfect' in query:
        #     music_dir = 'C:\\Users\\siddhant\\Downloads\\music'
        #     songs = os.listdir(music_dir)
        #     print(songs)
        #     os.startfile(os.path.join(music_dir, songs[1]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"{MASTER} the time is {strTime}")

        elif 'open visual studio code' in query:
            codePath = "C:\\Users\\siddhant\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'thank you' in query:
            greet = "Always a pleasure to serve you sir!. Anything else?"
            speak(greet)
            # exit()

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif 'Whats up?' in query:
            wu = "Just doing my thing sir!"
            speak(wu)

        elif 'bye' in query:
            stop = "Hope u enjoyed my services. Goodbye!"
            speak(stop)
            exit()

        elif 'email' in query:
            speak('Who is the recipient')
            recipient = takeCommand()

    # try:
            if 'myself' in recipient:

                speak('What should i say?')
                content = takeCommand()

                mail = smtplib.SMTP('smtp.gmail.com', 587)
                mail.ehlo()

                mail.starttls()

                mail.login('siddhant.zaveri@sakec.ac.in',
                           'enter your password')

                mail.sendmail('sid', 'zaverisid934@gmail.com', content)

                mail.close()

                speak('email sent')

    # except:
    #     e = "I am not able to send the email right now"
    #     speak(e)

        else:
            query = query
            speak('Searching...')
            try:
                try:
                    speak('Just a minute sir.... ')
                    res = client.query(query)
                    results = next(res.results).text
                    speak('Got it!')
                    print(results)
                    speak(results)

                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('Just a minute sir...')
                    speak('Got It!')
                    print(results)
                    speak(results)

            except:
                url = "google.com"
                chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
                webbrowser.get(chrome_path).open(url)
