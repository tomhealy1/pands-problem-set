#Solution to Problem No. 6
#Variation of the int input request from user except asks for a string
import string
import re
y_words = str(input("Please enter a sentence: "))

#split y_works into separate words using .split()
words = y_words.split(' ')

#loops through every 2nd item in words satrting from zero
for i in range(1,len(words), 2):
    #prints i taken the list words
    print(words[i])

















