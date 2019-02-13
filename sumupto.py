#x = integer with input call
x = int(input("Please enter a positive integer: "))

#if condition for negative integer
if (x < 0):
    print("Check your number and run again")
#if 0 then sum is = to 0
else:
    sum = 0 #start of range 
#while the condition x greater 0 is true then, 
    while(x > 0):
        sum += x #adds all integers in range plus x
        x -= 1
    print("The sum is",sum)