class Person(object):
    #constructor/initialization method
    def _init_(self,name,age):
        self.name = name
        self.age = age
    def _str_(self):
        return "My name is {0}. I am {1} years old".format(self.name, self.age)
class Military(Person):
    def _init_(self, name, age, rank):
        Person._init_(self, name, age) #calling a class method (initializing variables)
        self.rank = rank
    def _str_s(self):
        #overridding (same name as Parent class), when you call object of Military Class will look for methods corresponding the name, then go to parent class
        return Person._str(self) + "I am a {0}}".format(self.rank)
class Teacher(Person):
    def _init_(self, name, age, sub):
        Person._init_(self, name, age) #calling a class method (initializing variables)
        self.sub = sub
    def _str_s(self):
        #overridding (same name as Parent class), when you call object of Military Class will look for methods corresponding the name, then go to parent class
        return Person._str(self) + "I teach{0}}".format(self.sub)
class Student(Person):
    def _init_(self, name, age, loans):
        Person._init_(self, name, age) #calling a class method (initializing variables)
        self.loans = loans
        
    
