import datetime
import time

alarm_time = None
current_time = None

def set_alarm():
    global alarm_time
    hours = int(input("Entrez les heures: "))
    minutes = int(input("Entrez les minutes: "))
    seconds = int(input("Entrez les secondes: "))
    alarm_time = datetime.datetime.now().replace(hour=hours, minute=minutes, second=seconds)
    print("Alarme enregistrée !!")

def set_time():
    global current_time
    while True:
        hours = int(input("Entrez les heures: "))
        minutes = int(input("Entrez les minutes: "))
        seconds = int(input("Entrez les secondes: "))
        if 0 <= hours <= 24 and 0 <= minutes <= 59 and 0 <= seconds <= 59:
            current_time = datetime.datetime.now().replace(hour=hours, minute=minutes, second=seconds)
            break
        else:
            print("Entrez des heures, minutes et secondes valides.")

def clock():
    global current_time
    while True:
        current_time += datetime.timedelta(seconds=1)
        time_str = current_time.strftime("%H:%M:%S")
        print(f"         |      {time_str}     |")
        time.sleep(1)
        if alarm_time and alarm_time.strftime("%H:%M:%S") == current_time.strftime("%H:%M:%S"):
            print("DRING DRING DRING")
            reset_question = input("Relancer l'horloge ? (oui ou non) : ")
            if reset_question == "oui":
                set_alarm()
            else:
                        print(f"         |      {time_str}     |")


def main():
    alarm_question = input("Voulez vous mettre en place une alarme ? oui ou non : ")
    if alarm_question == "oui":
        set_alarm()
    set_time()
    clock()

main()

    