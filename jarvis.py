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
import math
import smtplib
import operator
from twilio.rest import Client
import cv2
import wmi
import tkinter as tk
import pywhatkit
import pyjokes
import pyautogui
import requests
import numpy as np
import subprocess
import randfacts
import speedtest
import PyPDF2
import pytube 
import psutil
from pywikihow import exceptions, search_wikihow
from bs4 import BeautifulSoup
# from PyQt5 import QtWidgets, QtCore, QtGui
# from PyQt5.QtCore import QTimer, QTime, QDate, Qt 
# from PyQt5.QtGui import QMovie
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
# from PyQt5.QtWidgets import *
# from PyQt5.uic import loadUiType
from requests import get

MASTER = 'Sid'

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices)
engine.setProperty('voice', voices[0].id)
# engine.setProperty('rate', 180)

client = wolframalpha.Client('K6Y537-G9KHELRWVH')


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    speak("Hello, This is Jarvis")
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

def pdf_reader():
    book = open('paper.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(book)
    pages = pdfReader.numPages
    speak(f"Total number of pages in this book are {pages}")
    speak("Sir please enter the page number i have to read")
    pg = int(input("Please enter the page number: "))
    page = pdfReader.getPage(pg)
    text = page.extractText()
    speak(text)

def cpu():
    cpu = str(psutil.cpu_percent())
    print(cpu)
    speak(f"You have used {cpu} of cpu")

def battery():
    battery = psutil.sensors_battery().percent 
    print(battery)
    speak(f"We have {battery} percent of battery left") 
    if battery >= 75:
        speak("Sir, We have enough battery to continue with our work")
    elif battery >=40 and battery < 75:
        speak("Sir, we have a considerable amont of battery to continue working")
    elif battery >=15 and battery < 40:
        speak("Sir, we might not have sufficient power to work. Please connect your charger")
    elif battery < 15:
        speak("Sir, the system will shut down soon. Kindly connect the charger immidiately")




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

        elif 'battery' in query:
            battery()

        elif 'cpu' in query:
            cpu()

        elif 'fact' in query or 'facts' in query:
            x = randfacts.getFact()
            print(x)
            speak("Did you know that, " +x)
        
        elif 'speed test' in query:
            st = speedtest.Speedtest()
            dl = speedtest.download()
            up = speedtest.upload()
            speak(f"Sir we have {dl} bit per second downloading speed and {up} bits per second uploading speed")
            # try:
            #     os.system('cmd /k "speedtest"')

            # except:
            #     speak("Sir, there is no internet connection")

        elif 'take a note' in query or 'write' in query or 'note' in query:
            speak("What should i write sir?")
            note = takeCommand()
            remember = open("data.txt", 'w')
            remember.write(note)
            remember.close()
            speak("I have noted that" + note)

        elif 'any reminders' in query or 'reminder' in query:
            remember = open('data.txt', 'r').read()
            speak("You told me to remember that" + remember)


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

        elif 'record my screen' in query:
            speak("Okay sir, starting with screen recording")
            speak("Press Q to stop recording")
            resolution = (1920, 1080)
            codec = cv2.VideoWriter_fourcc(*"XVID")
            filename = "Recording.avi"
            fps = 60.0
            out = cv2.VideoWriter(filename, codec, fps, resolution)
            cv2.namedWindow("Live", cv2.WINDOW_NORMAL)
            cv2.resizeWindow("Live", 480, 270)
            while True:
                img = pyautogui.screenshot()
                frame = np.array(img)
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                out.write(frame)
                cv2.imshow('Live', frame)
                if cv2.waitKey(1) == ord('q'):
                    break
            out.release()
            cv2.destroyAllWindows()

        elif 'ip address' in query:
            ip = get('https://api.ipify.org').text
            speak(f"your IP Address is {ip}")

        elif 'system information' in query:
            c=wmi.WMI()
            my_system = c.Win32_ComputerSystem()[0]
            print(f"Manufacturer: {my_system.Manufacturer}")
            speak(f"Manufacturer: {my_system.Manufacturer}")
            print(f"Model: {my_system.Model}")
            speak(f"Model: {my_system.Model}")
            print(f"Name: {my_system.Name}")
            speak(f"Name: {my_system.Name}")
            print(f"Number of Processors: {my_system.NumberOfProcessors}")
            speak(f"Number of Processors: {my_system.NumberOfProcessors}")
            print(f"SystemType: {my_system.SystemType}")
            speak(f"SystemType: {my_system.SystemType}")
            print(f"SystemFamily: {my_system.SystemFamily}")
            speak(f"SystemFamily: {my_system.SystemFamily}")

        elif 'send message' in query or 'send a message' in query:
            pywhatkit.sendwhatmsg('number with countrycode', 'Content of the message', 23, 55)

        elif 'send text message' in query:
            speak("Sir, What should i say?")
            msz = takeCommand()

            account_sid = 'AC577bb2308196bbb72d207be0d6e6c053'
            auth_token = '095623c7cd5b15cae116e6866e8331ab'
            client = Client(account_sid, auth_token)

            message = client.messages \
                .create(
                    body = msz,
                    from_='+19165028175',
                    to='+917678060767'
                )

            print(message.sid)
            speak("The message has been sent successfully")



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

        elif 'thank you' in query or 'thanks' in query:
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

        elif 'hide all files' in query or 'hide this folder' in query or 'visible for everyone' in query:
            speak("Sir, please tell me whether you want to hide this folder or make it visible for everyone")
            condition = takeCommand().lower()
            if 'hide' in condition:
                os.system("attrib +h /s /d")
                speak("Sir all your files are now hidden")

            elif 'visible' in condition:
                os.system("attrib -h /s /d")
                speak("Sir, all your files are now visible to everyone.")

            elif 'leave it' in condition or 'leave for now' in condition:
                speak("ok sir!")

        elif 'read pdf' in query or 'read a pdf' in query or 'pdf' in query:
            pdf_reader()

        elif 'activate how to do mode' in query:
            speak("How to do mode is now activated")
            while True:
                speak("Please tell me what do you want to know")
                how = takeCommand()
                try:
                    if "exit" in how or "close" in how:
                        speak("okay sir, how to do mode is now deactivated")
                        break
                    else:
                        max_results = 1
                        how_to = search_wikihow(how, max_results)
                        assert len(how_to) == 1
                        how_to[0].print()
                        speak(how_to[0].summary)
                except Exception as e:
                    speak("Sorry sir i am not able to find this at this moment")
            


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

        elif 'do some calculation' in query or 'can u calculate' in query or 'calculate' in query or 'calculation' in query:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                speak("Sir, what do you want me to calculate, example: 3 plus 3")
                print("listening....")
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
            my_string=r.recognize_google(audio)
            print(my_string)
            def get_operator_fn(op):
                return{
                    '+' : operator.add,
                    '-' : operator.sub,
                    'X' : operator.mul,
                    'divided by' : operator.__truediv__,
                }[op]
            def eval_binary_expr(op1, oper, op2):
                op1,op2 = int(op1), int(op2)
                return get_operator_fn(oper)(op1, op2)
            speak("your result is")
            print(eval_binary_expr(*(my_string.split())))
            speak(eval_binary_expr(*(my_string.split())))

        elif 'temperature' in query:
            search = "temperature in mumbai"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div", class_="BNeawe").text
            speak(f"current {search} is {temp}")

        elif 'download video' in query:
            speak("Sir please enter the link of the video that you want to download")
            link = input("Paste the link here: ")
            yt = pytube.YouTube(link)
            stream = yt.streams.first()
            stream.download()
            speak("Your video has been successfully downloaded inside the folder")


        elif 'bye' in query or 'goodbye' in query:
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
        #         password = 'your password'
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
