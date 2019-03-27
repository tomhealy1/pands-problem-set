#Solution to Problem 9
#Tom Healy
#Added in Week 7 lessons, Created a file with first few paragraphs of Moby-Dick, 'r' denotes read and assigns it to var book

#Added in Week 9 lessons on using sys.argv to read file name form CLI
import sys

#If the number of commands from the command is less thn 2 then it will print an error message 
if len(sys.argv) !=2:
    print("Please enter a file name")
else:
    fname = sys.argv[1]
    print(fname)

#Adding in try and except error handling from the 
try:
    with open(fname, 'r') as book:
#Uses readlines statement to assign the lines in book to new arugment book1 
        book1 = book.readlines()
#Same as secondstring problem, use the range and len function return every 2nd line
    for i in range(0, len(book1), 2):
        print(book1[i])
#UnIndented to add the message about the file closing
    print("The file has now closed")

#Adding error handling from https://docs.python.org/3.7/tutorial/errors.html#tut-handling
except FileNotFoundError:
    print("That file could not be found, please make sure you have the correct file")
