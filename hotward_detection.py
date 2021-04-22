import os
import speech_recognition as sr





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

        except:
            # e = "I didnt quite get you, Please Say that again"
            # speak(e)
            # print("Say That Again Please....")
            return "None"

        return query.lower()

while True:
        wake_Up = takeCommand()

        if "wake up" in wake_Up:
            os.startfile('C:\\Users\\siddhant\\OneDrive\\Desktop\\Jarvis Project\\Virtual-Assistant\\jarvis.py')

        else:
            print("Nothing.....")