class fraction(object):
    def__init__(self,numer, denom):
        self.numer = numer
        self.denom = denom
    def__str__(self):
        #print our string representation of numerator and denominator separated by a slash- to resemble a fraction
        return str(self.numer) + ' / ' + str(self.denom)
    def getNumer (self):
        return self.numer
    def getDenom (self):
        return self.denom
    def__add__(self,other):
        numerNew = other.getDenom()* self.getNumer*() \
                   other.getnumer()* self.getDenom()
        denomNew = other.getDenom()* self.getDenom()
        return fraction(numberNew, denomNew)
    
