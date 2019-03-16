#Solution to problem 5 
#Tom Healy 
#Ask user for postive integer
num = int(input("Please enter a positive integer: "))
#if the inputted number is great than 1
if num > 1:
    for i in range(2, num):     #create list of numbers between 2 and itself
        if num % i == 0:   #if the remainder of num / any number in list is true to zero then it is not prime  
            print(num , "is not prime")
            break
    else:
        print(num, "is prime number")
else:
    print("Please enter a greater positive number")