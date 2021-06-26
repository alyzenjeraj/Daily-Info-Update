from datetime import datetime

def checkTime():
    if datetime.now().strftime("%H") >= 7 and datetime.now().strftime("%H") <= 11 and datetime.now().strftime("%M") == 30:
        print("Drink Water!")
    else:
        pass