#Solution to Problem 8
#Need to rename as it was trying to import this file
import calendar
from datetime import datetime
#Same function as from Problem 2
now = datetime.now()
#Renamed the newly formatted time to now1
now1 = now.strftime("%A, %B %d %Y at %H:%M %p")
print(now1)





