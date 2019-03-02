#Solution to Problem 9

#Created a file with first few paragraphs of Moby-Dick 
book = open('C:\\Users\\Teamwork\\Desktop\\Assessments\\pands-problem-set\\moby-dick.txt')
#Uses readlines statement to assign the lines in book to new arugment book1 
book1 = book.readlines()
#Same as secondstring problem, use the range and len function return every 2nd line
for i in range(0, len(book1), 2):
    print(book1[i])



