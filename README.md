# Pands-problem-set
### HDip in Data Analytics 2019 
### Tom Healy 

This repo contains the my solution to the Problem set for the Programming and Scripting module at GMIT.

[See here for the Problem set and instructions](https://github.com/ianmcloughlin/problems-pands-2019/raw/master/problems.pdf)

### How to download this repo
1. Go to Github
2. Open [this](https://github.com/tomhealy1/pands-problem-set)
3. Click the download button

### How to run the code
1. Make sure you have Python (Anaconda Preferable) installed
2. Open the CLI (Cmder preferable)
3. Type "python" and filename e.g. $ python sumupto.py
4. Enter input (string, float, int)
5. Review output

### The list of problems and brief outlines of solution 
<p>1. sumupto.py</p> 
<p>The problem is to request an input (integer) from the user and return printed to the screen the sum of all the values between
   one and that number. I used a "while" to accomplish this (while x is greater than zero) and added an if func when x is less that zero. 
   The code adds the numbers in the range and then stops when x is zero.</p>
<p>2. begins-with-t.py</p>
<p>The problem here is to write a program that returns to the screen whether today begins with a "T" or not. I import the calendar mod and datetime mod. I use the datetime.now() and assign it to now. I do the same with weekday with today's weekday assigned to it. The days are returned as a int from 0 to 6. Tuesday and Thurday is 1 and 3 respectively. So we can use an if statement to then check if it is equal to 1 or 3. I added the else statement to if loop to deal with the non Tuesday and Thurday days.
<p>3. divisor.py</p>
<p>Problem 3 print all numbers between 1000 and 10,000 that are divisable by 6 and not 12. First we create the range for the var "num" between 1,00 and 10,000. We then use an "if" statement to check if each num can divided by 6 without a remainder and 12 with a remainder and then we print the num that fits those conditions to the screen.</p>
<p>4. collatz.py</p>
<p> This program asks the user to input a positive integer. The program then loops through a series of steps where if the value is even, it divides by two, if the values is odd, it will multiply it by 3 and add one. The program stops at one. I use the input func to request an int. If the integer is less that 0, it will ask for another. If the int is greater than 0, we use an if statement to check if the number is even (divide by 2 and check that there is no remainder). If even a new value is then passed to x (dividved by 2). If odd x is passed a new value after x is multplied by 3 and add one. The loop keeps going until it get to one because of the while condition.</p> 
<p>5. primes.py</p>
<p>Problem 5 is a program to check if an inputted value is a prime number or not. First, we ask the user for an integer. If the integer is greater than one, it creates a range between 2 and the inputted value. If the "num" divided by any int in the range then it is not prime. We have an else condition for all other members of the list that are prime.
<p>6. secondstring.py</p>
<p>Problem 6 asks for a string from the user. We then have a program that will return every 2nd word and print to the screen almost like a new sentence. First, we import the string module. We then assign the string input to y_words. We then use the split function to split the input using space as a separator and assign it to the words var. We then create a range beginning at the 2nd word in the range and goes through every 2nd word. It then prints those words to the screen.
<p>7. sqaureroot.py</p>
<p>The squareroot problem is one where it asks the user for an input and then returns an approximation of the squareroot. First, we use the input prompt to request the float. We import the math module, and if the input is greater than 0 we continue. We assign the square root value for x to z. We then print the return value using a format that drops the decimal places after the first place after the point. </p>
<p>8. datetime.py</p>
<p>Problem 8 print today's date and time formatted in a certain way. We import calendar and datetime modules. We assign datetime.now() to now. We then reformat now to the format outlined in the problem ("%A, %B %d %Y at %H:%M %p"). The format is (Weekday(Monday, Tuesday...., Month(January, February)..., Date (10th, 11th), Year (2019), at , Time (5:33 pm) ).</p>
<p>9. second.py</p>
<p>Problem 9 requires a program to read in a text file and then return every 2nd line. We use "with open.... as book" to read in the file as book. We then assign the output of readlines to the var book1. We then use the range function to return every 2nd line in book 1 using a similar function in prob 6. We then print the output to the screen and then we unindent to close the loop.</p>
<p>10. Problem-10.py</p>
<p>This problem plots three functions. 


### References


1. [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/)

2. [Python for Data Analysis, 2e](https://www.bookdepository.com/Python-for-Data-Analysis-2e-Wes-McKinney/9781491957660?redirected=true&utm_medium=Google&utm_campaign=Base1&utm_source=IE&utm_content=Python-for-Data-Analysis-2e&selectCurrency=EUR&w=AFFPAU96Q2VP05A80381&pdg=pla-104399445939:kwd-104399445939:cmp-711089934:adg-37476253379:crv-163904732377:pid-9781491957660:dev-c&gclid=CjwKCAiAiJPkBRAuEiwAEDXZZT72W6wFgoJjZ876F2c0lLHOjyhXNT-ybD4lmSzpbWpF6qrAi0zIDhoCDdMQAvD_BwE)

3. [Python Tutorial](https://docs.python.org/3/tutorial/)

4. [w3 Online Coding School](https://www.w3schools.com/python/default.asp)

5. Learn Python the Hard Way

6. Learning Python 5th Edition

7. Python in a Nutshell
