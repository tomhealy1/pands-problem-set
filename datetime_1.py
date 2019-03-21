#Solution to Problem 8
#Tom Healy
#Need to rename as it was trying to import this file, learned valuable lesson: Dont name your files the same as pkgs, mods or other python goodies!!
import calendar
from datetime import datetime
#Same function as from Problem 2, passed datetime.now and assigned it to var now
now = datetime.now()
#Renamed the newly formatted time to now1
now1 = now.strftime("%A, %B %d %Y at %H:%M %p")
print(now1)





