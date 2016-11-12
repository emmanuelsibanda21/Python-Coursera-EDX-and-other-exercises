class fraction(object):
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom
    def __str__(self):
        #print our string representation of numerator and denominator separated by a slash- to resemble a fraction
        return str(self.numer) + ' / ' + str(self.denom)
    def getNumer (self):
        return self.numer
    def getDenom (self):
        return self.denom
    def __add__(self,second):
        newnum = self.numer*second.denom + self.denom*second.numer
        newdenom = second.denom* self.denom
        return fraction(newnum, newdenom)
    def __repr__(self):
        return "fraction(%d, %d)" % (self.numer, self.denom)

    
