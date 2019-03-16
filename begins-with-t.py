#Solution to Problem 2
#Tom Healy
import calendar #import calendar module
from datetime import datetime #import datetime mod

now = datetime.now() #what is today's date and time

weekday = now.weekday() #weekday = today day

if weekday == 1: #if today's day is equal to Tuesday, print
    print("Yay today begins with a T")
elif weekday == 4:#if today is equal to Thursday print
    print("Yay today begins with a T")
else: #if today not equal to Tuesday or Thursday print else statement
    print("No today does not begin with a T")





