'''
8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes, sort and print the resulting words in alphabetical order.
You can download the sample data at http://www.pythonlearn.com/code/romeo.txt

Check Code
'''
#open and read file
fname = raw_input("Enter file name: ")
fh = open(fname, 'r')
frame = []
final_list = []
#read file
fh_list = fh.read().rstrip()
#run through the list and add all words to frame list
for word in fh_list.split():
    frame.append(word)
    #sort frame list alphabetically
    frame.sort()
#remove duplications by adding all elements to new list
for i in frame:
    if i not in final_list:
        final_list.append(i)
print final_list
