import datetime
import winsound
from playsound import playsound

def alarm(Timing):
    altime = str(datetime.datetime.now().strptime(Timing,"%I:%M %p"))
     
    altime = altime[11:-3]
    print(altime)

    Horeal = altime[:2]
    Horeal = int(Horeal)
    Mireal = altime[3:5]
    Mireal = int(Mireal)
    print(f"Done, the alarm is set for {Timing}")

    while True:
        if Horeal == datetime.datetime.now().hour:
            if Mireal == datetime.datetime.now().minute:
                print("alarm is running")
                playsound('alarm_tone.mp3', winsound.SND_LOOP)

            elif Mireal<datetime.datetime.now().minute:
               break

if __name__ == '__main__':
    alarm('10:47 PM')
