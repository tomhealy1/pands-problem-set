#Solution to collatz.py problem
x = int(input("Please enter a positive integer: "))
if x < 0:
    print("Please enter a positive number")
else:
    pass

while x > 1:
    if x % 2 == 0:
        x = x // 2
    else:
        x = 3 * x + 1
    print(x)


