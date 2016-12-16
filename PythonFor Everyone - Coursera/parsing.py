import re
ruck = []
count = 0
open_file = open('regex_sum_315748.txt')
#read contents of file as a string
string_file = open_file.read()
#find all integers and store integers in integers variable as a list
integers = re.findall('[0-9]+', string_file)
print integers
#run through all the strings in integers list
for number in integers:
    #keep tally of all the strings in integers
    count +=1
    #convert strings to integers
    number = int(number)
    #add all integers to ruck variable
    ruck.append(number)
print 'The total number is:', sum(ruck)
print 'The average is:', sum(ruck)/count



#how do I add numbers in a list??
