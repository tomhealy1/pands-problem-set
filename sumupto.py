#x = asks for user to input positive integer
x = int(input("Please enter a positive integer: "))

total = 0 #total variable starts at 0 
#while x is less than 0 
while x > 0:
    total = total + x #LHS new total is equal to previous value + x
    x = x - 1 #LHS x is equal to x - 1 , while x is less than 0, this will continue to run
    
print(total) #once the while loop has finished, it print total