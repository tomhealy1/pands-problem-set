#First import package for datetinme
import datetime
#Set condition True for if today begins with T
if datetime.datetime.today().weekday()== 1:
    print("Yes, today begins with a T.")
elif datetime.datetime.today().weekday()== 3:
    print("Yes, today begins with a T.")

    #Condition for false
else datetime.datetime.today().weekday()== 0:
    
    print("No - today does not begin with a T.")



