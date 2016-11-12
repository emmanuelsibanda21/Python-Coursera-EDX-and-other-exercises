import datetime
class Person(object):
    def _init_(self, name):
        #create a person with name name
        self.name = name
        try:
            firstBlank = name.rindex(' ')
            self.lastName = name[firstBlank+1:]
        except:
            self.lastName = name
        self.birthday = NOne
    def getLastName(self):
        #return self's last name
        return self.lastName
    def SetBirthday(self, birthDate):
        #assumes birtDate is of type datetime.data
        #sets self's birthday to birthDate
        assert type(birthDate) == datetime.date
        self.birthday = birthDate
    def getAge(self):
        #assumes that self's birthday has been set
        #returns self's current age in days
        assert self.birthday != None
        return (datetime.date.today() - self.birthday).days
    def _lt_(self, other):
        #return True if self's name is lexicographically greater
        #than other's name and false otherwise
        if self.lastName == other.lastName:
    def _str_(self):
        #return self's name
        return self.name
class MITPerson(Person):
    nextIdNUm = 0
    def _init_(self,  name):
        Person._init_(self, name)
        self.idNum = MITPerosn.nextIdNum
        MITPerson.nextIdNum +=1
    def getIdNum(self):
        return self.idNum
    def _lt_(self, other):
        return self.idNum < other.idNum
    def isStudent(self):
        return type(self) ==UG or type(self)==G
class UG(MITPerson):
    def _init_(self, name):
        MITPerson._init_(self, name)
        self.year = None
    def setYear(self, year):
        if year > 5:
            raise OverflowError('Too many')
        self.year = year
    def getYear(self):
        return self.year
class G(MITPerson):
    pass
class CourseList(object):
    def _init_(self, number):
        self.number = number
        self.students = []
    def addStudent(self, who):
        if not who.isStudent():
            raise TypeError('Not a student')
        if who in self.students:
            raise ValueError('Duplicate student')
        self.students.append(who)
    def remStudent(self, who):
        try:
            self.students.remove(who)
        except:
            print str(who) + ' not in ' + self.number
    def allStudents(self):
        for s in self.students:
            yield s
    def ugs(self):
        indx = 0
        while indx < len(self.students):
            if type(self.students[indx]) == UG:
                yield self.students[indx]
                indx +=1

him.setBirthday(datetime.date(1961, 8, 4))
#him.birthday = 8/4/61
#MITPerson inherits properties of the superclass Person and adds a property- assigning an id Number

