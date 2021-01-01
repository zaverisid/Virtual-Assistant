import pyttsx3
import speech_recognition as sr
import datetime
import time
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
import pyautogui
import requests
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
        r.pause_threshold = 2  # press ctrl on pause threshhold to increse decrese sensitivity
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


def news():
    main_url = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=052dbc66de9c4123848e8603392016cf'

    main_page = requests.get(main_url).json()
    articles = main_page["articles"]
    head = []
    day = ["first", "second", "third", "fourth", "fifth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        print(f"today's {day[i]} news is: {head[i]}")
        speak(f"today's {day[i]} news is: {head[i]}")


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

        elif 'news' in query:
            speak("Please wait sir, Fetching the latest news")
            news()

        elif 'open command prompt' in query:
            os.system('start cmd')

        elif 'close command prompt' in query:
            speak("ok sir, Closing command prompt")
            os.system("taskkill /f /im cmd.exe")

        elif 'shutdown the system' in query:
            speak("ok sir, Shutting down")
            os.system("shutdown /s /t 5")

        elif 'sleep off' in query:
            speak("ok sir, Sleeping")
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

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
            pywhatkit.sendwhatmsg('your number', 'your message', 14, 12)

        elif 'switch the window' in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")

        elif 'play' in query:
            song = query.replace('play', '')
            speak('playing' + song)
            pywhatkit.playonyt(song)

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

        elif 'instagram profile' in query or 'profile on instagram' in query:
            speak("Sir please enter the username correctly")
            name = input("Enter username here = ")
            webbrowser.open(f"www.instagram.com/{name}")
            speak(f"here is the profile of the user {name}")
            time.sleep(5)

        elif 'take screenshot' in query or 'take a screenshot' in query or 'screenshot' in query:
            speak("Sir, please tell me the name for this screenshot file")
            name = takeCommand().lower()
            speak("Sir, please hold the screen for a few seconds, i am taking the screenshot")
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("The screenshot has been taken and saved in our main folder")


        elif 'where am i' in query or 'where are we' in query:
            speak("Wait sir, Let me check")
            try:
                ipAdd = requests.get('https://api.ipify.org').text
                print(ipAdd)
                url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                city= geo_data['city']
                country= geo_data['country']
                speak(f"sir, i am not sure but we are in {city} city of {country}")
            except Exception as e:
                speak("Sorry sir, I cannot fetch the information at this moment")
                pass


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
                           'your password')

                mail.sendmail('sid', 'zaverisid934@gmail.com', content)

                mail.close()

                speak('email sent')

    # except:
    #     e = "I am not able to send the email right now"
    #     speak(e)
        # elif 'email to me' in query:
        #     speak("Sir,what should i say?")
        #     query=takeCommand().lower()
        #     if "send a file " in query:
        #         email = 'siddhant.zaveri@sakec.ac.in'
        #         password = 'innova5639'
        #         send_to_email = 'zaverisid934@gmail.com'
        #         speak("Ok sir, what is the subject of this email?")
        #         query=takeCommand().lower()
        #         subject = query
        #         speak("And what is the message for this email?")
        #         query2 = takeCommand().lower()
        #         message = query2
        #         speak("Sir, please enter the correct path of the file into the shell")
        #         file_location = input("please enter the path here: ")

        #         speak("Please wait I am sending the email now...")

        #         msg = MIMEMultipart()
        #         msg['From'] = email
        #         msg['To'] = send_to_email
        #         msg['Subject'] = subject

        #         msg.attach(MIMEText(message, 'plain'))

        #         filename = os.path.basename(file_location)
        #         attachment = open(file_location,"rb")
        #         part = MIMEBase('application', 'octet-stream')
        #         part.set_payload(attachment.read())
        #         encoders.encode_base64(part)
        #         part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

        #         msg.attach(part)

        #         server.smtplib.SMTP('smtp.gmail.com', 587)
        #         server.ehlo()
        #         server.starttls()
        #         server.login('siddhant.zaveri@sakec.ac.in','innova5639')
        #         text=msg.as_string()
        #         server.sendmail(email,send_to_email,text)
        #         server.quit()
        #         speak("email has been sent")

        #     else:
        #         email = 'siddhant.zaveri@sakec.ac.in'
        #         password = 'innova5639'
        #         send_to_email = 'zaverisid934@gmail.com'
        #         message=query

        #         server.smtplib.SMTP('smtp.gmail.com', 587)
        #         server.starttls()
        #         server.login('siddhant.zaveri@sakec.ac.in','innova5639')
        #         server.sendmail(email,send_to_email,text)
        #         server.quit()
        #         speak("email has been sent")

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
