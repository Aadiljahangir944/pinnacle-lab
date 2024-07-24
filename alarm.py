import datetime
import time
from playsound import playsound

alarmhr =int(input("Entre Hour: "))
alarmmin=int(input("Entre Minutes: "))
alarm = input("am / pm: ")
alarm_tone = input("Entre alarm tone path: ")


if alarm=="pm":
    alarmhr+=12

while True:
    if alarmhr == datetime.datetime.now().hour and alarmmin==datetime.datetime.now().minute:
        print("Utho kahil ｡^‿^｡")
        playsound(alarm_tone)

        while True:
            snooze_input = input("Do you want to snooze? (yes/no): ").strip().lower()
            snooze_duration=int(1)
            
            if snooze_input == "yes":
                print(f"Snoozing for {snooze_duration} minutes...")
                time.sleep(snooze_duration*60)
                print("kambakht kahil utho (ง’̀-‘́)ง")
                playsound(alarm_tone)
                
            elif snooze_input == "no":
                print("Alarm dismissed!")
                break
        break
time.sleep(1)