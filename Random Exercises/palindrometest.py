def isPal(x):
    if type(x) == str:
        tempo = [i for i in x]
        test = [i for i in x]
        test.reverse()
        if test == tempo:
            print "This is a palindrome"
        else:
            print "This is not a palindrome"
    elif type(x) == list:
        tempo_2 = [i for i in x]
        test_2 = [i for i in x]
        tempo_2.reverse()
        if tempo_2 == test_2:
            print "This is a palindrome"
        else:
            print "This is not a palindrome"
        
