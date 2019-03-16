#Solution to problem 3
#Tom Healy
#Create range with range function to specify nums between 1000 and 10000
for num in range(1000,10000):
    #if true statement for the remainder for 6  ( Half way there :-)
    if num % 6 == 0 and num % 12 != 0:
        print(num)
    
        
       
