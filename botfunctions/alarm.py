from datetime import datetime
timers = []
def initTimer(minutes): #minutes = minutes from now
    global timers
    currentTimeHour = datetime.now().strftime("%H") #24 hour time
    currentTimeMinute = datetime.now().strftime("%M")
    hours = minutes // 60
    minutes -= hours * 60
    targetTimeMinute = currentTimeMinute + minutes
    if targetTimeMinute >= 60:
        targetTimeMinute -= 60
        hours += 1
    targetTimeHour = currentTimeHour + hours
    if targetTimeHour >= 24:
        targetTimeHour -= 24
    targetTime = [targetTimeHour, targetTimeMinute]
    timers.append(targetTime)

def checkTime():
    global timers
    for i in range(len(timers)):
        if timers[i][0] == datetime.now().strftime("%H") and timers[i][1] == datetime.now().strftime("%M"):
            print("Alarm!")
            timers.pop(i)
        else:
            pass

