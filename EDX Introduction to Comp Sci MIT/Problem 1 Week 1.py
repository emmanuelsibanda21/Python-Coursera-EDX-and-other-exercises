'''
Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:

'''

def vowels(s):
    a = s.count("a")
    e = s.count("e")
    i = s.count("i")
    o = s.count("o")
    u = s.count("u")
    total = a+e+i+o+u
    print "Number of vowels:", total
