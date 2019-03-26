#Solution to Problem 9
#Tom Healy
#Added in Week 7 lessons, Created a file with first few paragraphs of Moby-Dick, 'r' denotes read and assigns it to var book

import sys

print("The name of the file is: ", sys.argv[1])

with open('C:\\Users\\Teamwork\\Desktop\\Assessments\\pands-problem-set\\moby-dick.txt', 'r') as book:
#Uses readlines statement to assign the lines in book to new arugment book1 
    book1 = book.readlines()
#Same as secondstring problem, use the range and len function return every 2nd line
    for i in range(0, len(book1), 2):
        print(book1[i])
#UnIndented to add the message about the file closing
print("The file has now closed")




