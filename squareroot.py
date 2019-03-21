#Solution to Problem 7
#Tom Healy
#import math mod to use square root function
import math 
#Asks user for input as float
x = float(input("Please enter a positive number: "))
#Add if condition for x greater that 0
if x > 0:
    z = math.sqrt(x) #square root value for x now becomes z and formatted to one decimal place
    print("The square root of", x, "is approx.", "{:.1f}".format(z))
#Added elif statement
elif x < 0:
    print("Please use a positive number")
