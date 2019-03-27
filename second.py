#Solution to Problem 9
#Tom Healy
#Added in Week 7 lessons, Created a file with first few paragraphs of Moby-Dick, 'r' denotes read and assigns it to var book

#Added in Week 9 lessons on using sys.argv to read file name form CLI (Had to play around a lot to get it working)
import sys

#If the number of commands from the command is less thn 2 then it will print an error message 
try:
# count the number of arguments supplied via command-line
    if len(sys.argv) == 2: 
        with open(sys.argv[1], 'r') as book:
#Uses readlines statement to assign the lines in book to new arugment book1 
            book1 = book.readlines()
#Same as secondstring problem, use the range and len function return every 2nd line
            for i in range(0, len(book1), 2):
                print(book1[i])
#UnIndented to add the message about the file closing
        print("The file has now closed")
#Added the else and pass ststement to close the if loop
    else:
        pass
        print ("Please enter a text filename")
        sys.exit()
#Added in except statement File error handling from https://docs.python.org/3.7/tutorial/errors.html#tut-handling
except FileNotFoundError:
    print("File does not exist, please try again")
