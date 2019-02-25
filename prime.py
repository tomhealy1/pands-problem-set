#Solution to problem 5 
#Ask user for postive integer
num = int(input("Please enter a positive integer: "))

#x is equal to inputted number floor divided by 2
x = num // 2

#while x is greater than 1 
while x > 1:
    #if inputted number / x's remainder is 0 then the number cant be prime as
    #as the it can be divided 
        if num % x == 0:
        print(num, "is not prime")
        break
else:
    print(num , "is prime")