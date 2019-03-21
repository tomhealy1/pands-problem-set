#Solution to Problem 1
#x = asks for user to input positive integer
#Tom Healy
x = int(input("Please enter a positive integer: "))

if x < 0:
    print("Please try a positive integer")


total = 0 #total variable starts at 0 
#while x is greater than 0 
while x > 0:
    total = total + x #LHS (Left hand side) new total is equal to previous value + x
    x = x - 1 #LHS x is equal to x - 1 , while x is greater than 0, this will continue to run
    
print(total) #prints the total iteratively to the screen and stops at 0 