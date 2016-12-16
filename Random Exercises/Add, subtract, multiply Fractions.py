class Fraction:
    """A class to represent a rational number"""
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom
    def get_numer(self):
        return self.numer
    def get_denom(self):
        return self.denom
    def is_fraction(self):
        if self.denom == 0 and self.numer == 0:
            raise ValueError("The number zero is not a fraction")
        elif self.denom > self.numer:
            raise ValueError("The denominator is greater than the numerator")
    def __add__(self, other):
        new_leftnumer = self.numer * other.denom
        new_rightnumer = other.numer * self.denom
        new_denom = self.denom * other.denom
        total_numer = new_leftnumer + new_rightnumer
        print (total_numer, "/", new_denom)
    def __sub__(self):
        new_leftnumer = self.numer * other.denom
        new_rightnumer = other.numer * self.denom
        new_denom = self.denom * other.denom
        total_numer = new_leftnumer + new_rightnumer
        print (total_numer, "/", new_denom)
    def simplify_frac (self):
        simple_denom = new_denom / self.denom
        simple_numer = total_numer / self.denom
        print (simple_numer, "/", simple_denom)
    def get_simplenumer (self):
        return simple_numer
    def get_simpledenom (self):
        return simple_denom
    
        
