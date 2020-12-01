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
import tkinter as tk
import pywhatkit as kit

MASTER = 'Sid'

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
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


# def sendmsg():
#     global num
#     global text
#     global time_h
#     global time_m
#     num = x.get()
#     text = y.get()
#     time_h = th.get()
#     time_m = tm.get()
#     root.destroy()
#     kit.sendwhatmsg(num, text, time_h, time_m)


def takeCommand():
    # it takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 2
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
            # webbrowser.open("youtube.com")
            url = "youtube.com"
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)

        elif 'open google' in query:
            url = "google.com"
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)

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

        elif 'play music' in query:
            music_dir = 'C:\\Users\\siddhant\\Downloads\\music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'play perfect' in query:
            music_dir = 'C:\\Users\\siddhant\\Downloads\\music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[1]))

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

        # elif 'send message' in query:
        #     root = tk.Tk()
        #     root.configure(bg="green")
        #     x = tk.StringVar()
        #     y = tk.StringVar()
        #     th = tk.IntVar()
        #     tm = tk.IntVar()

        #     root.geometry("300x200")
        #     root.title("Whatsapp using Python")
        #     label1 = tk.Label(root, text="Enter your number:").grid(row=0, column=0)
        #     label2 = tk.Label(root, text="Enter your text:").grid(row=1, column=0)
        #     label3 = tk.Label(root, text="Enter time in hour:").grid(row=2, column=0)
        #     label4 = tk.Label(root, text="Enter time in minute:").grid(row=3, column=0)

        #     entry1 = tk.Entry(root, textvariable=x).grid(row=0, column=1)
        #     entry2 = tk.Entry(root, textvariable=y).grid(row=1, column=1)
        #     entry3 = tk.Entry(root, textvariable=th).grid(row=2, column=1)
        #     entry4 = tk.Entry(root, textvariable=tm).grid(row=3, column=1)
        #     button = tk.Button(root, text="Send", command=sendmsg).grid(row=4, column=0)

        #     root.mainloop()

        # elif 'I love you bro' in query:
        #     love = "I love you 3000 Sir!"
        #     speak(love)

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

                mail.login('siddhant.zaveri@sakec.ac.in', 'enter your password')

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
                    results = wikipedia.summary(query, sentences= 2)
                    speak('Just a minute sir...')
                    speak('Got It!')
                    print(results)
                    speak(results)

            except:
                url = "google.com"
                chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
                webbrowser.get(chrome_path).open(url)
