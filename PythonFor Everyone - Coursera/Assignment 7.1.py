'''
7.1 Write a program that prompts for a file name, then opens that file and reads through the file, and print the contents of the file in upper case. Use the file words.txt to produce the output below.
You can download the sample data at http://www.pythonlearn.com/code/words.txt

Check Code
'''
# Use words.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
#strip whitespaces and add to list variable, then capital all elements in list vairable and store in capitalized variable
for i in fh:
    list = i.rstrip()
    capitalized = list.upper()
    print capitalized
