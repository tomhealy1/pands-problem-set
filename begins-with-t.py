#Solution to Problem 2
#Tom Healy
#Import calendar module
import calendar 

#Import datetime mod from datetime package
from datetime import datetime 

#what is today's date and time abd assigning that to the varible now
now = datetime.now() 

#Assigning today's weekday to the var weekday
weekday = now.weekday() 

#if today's day is equal to Tuesday, print "Yay today begins with a T". I could have used an "or" statement instead of a elif
if weekday == 1: 
    print("Yay today begins with a T")

#if today is equal to Thursday print "Yay today begins with a T"
elif weekday == 3:
    print("Yay today begins with a T")

#if today not equal to Tuesday or Thursday print else statement
else: 
    print("No today does not begin with a T")





