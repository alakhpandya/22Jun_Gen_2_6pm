# Monte Carlo Problem: What is the maximum path length for which we don't have to pay for the taxy on an average?
"""
from random import choice

def getRandomPath(pathLength):
    '''
    x = 0
    y = 0
    for i in range(pathLength):
        directions = ["up", "down", "left", "right"]
        d = choice(directions)
        if d == "up":
            y += 1
        elif d == "down":
            y -= 1
        elif d == "right":
            x += 1
        else:
            x -= 1

    return x, y
    '''
    x, y = 0, 0
    for i in range(pathLength):
        dx, dy = choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
        x += dx
        y += dy
    return x, y

# pathLength = 10
print("Length\tProbability")
for pathLength in range(11, 30):
    noPay = 0
    numberOfWalks = 10000
    for x in range(numberOfWalks):
        x, y = getRandomPath(pathLength)
        d = abs(x) + abs(y)
        if d <= 5:
            noPay += 1
    print(f"{pathLength}\t{noPay * 100/numberOfWalks}")
"""
# datetime
import datetime

"""
# print(dir(datetime))
# print(datetime.MINYEAR)
# print(datetime.MAXYEAR)

jenish = datetime.date(2023, 11, 18)
print(jenish)

print(jenish.year)
print(jenish.month)
print(jenish.day)

curr_date = datetime.date(2023, 6, 27)
print(curr_date)
print(jenish - curr_date)
"""
"""
bhavin = datetime.datetime(2023, 10, 6, 17, 25, 35, 345226)
# print(bhavin)

curr_date = datetime.datetime.now()
print(curr_date)
"""
# harshil = datetime.datetime(2023, 7, 29)
# print(harshil + 100)
# interval = datetime.timedelta(100, 0, 0, 0, 0, 12)
# print(harshil + interval)

# meet = datetime.datetime(2003, 2, 29)
meet = datetime.datetime(2023, 8, 16, 15, 30)
meet_bday = meet.strftime("%B %dth, %A, %y %I:%M %p")
print(meet_bday)

# Next class: strptime, time module etc
# HW:
"""
1. Create an app that takes date of birth of user (including year, month & day) and returns their age in days.
"""