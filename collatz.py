#Solution to collatz.py problem
#Tom Healy 
#Request an integer from user using input
x = int(input("Please enter a positive integer: "))

#Added condition for if the integer is not positive
if x < 0:
    print("Please enter a positive number")
#OK so I did not know what to add to the else statement here so I used pass and I wanted to use pass anyway :)
else:
    pass

#This is the bones of the assignment, while x is greater than 1
#the function will check if the input (x) is  even by using the modulus check
while x > 1:
    if x % 2 == 0:
#The x will be divided by 2 which will be the new value of x
        x = x // 2
#else condition for odd numbers
    else:
        x = 3 * x + 1
#added print function to hopefully print the new values assigned to x
    print(x)


