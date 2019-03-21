#Solution to Problem No. 6
#Tom Healy
#Variation of the int input request from user except asks for a string
#Import the string package and re (regular expression package)
import string
#import re I did not need this as I am not matching a regex
y_words = str(input("Please enter a sentence: "))

#split y_works into separate words using .split()
words = y_words.split(' ')

#Indexes from zero, strts counting from the 2nd member in the range and loops through every 2nd item in words starting from zero
for i in range(1,len(words), 2):
    #prints i taken the list words
    print(words[i])

















