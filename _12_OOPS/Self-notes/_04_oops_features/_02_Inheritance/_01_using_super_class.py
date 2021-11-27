# Super method is used to call the methods or variables of super class from the subclass when ever
# we have a requirement of accessing the super class method or variables


class Person:
    def __init__(self, fn, ln):
        self.fname = fn
        self.lname = ln

    def printname(self):
        print(self.fname, self.lname)


class Student(Person):
    def __init__(self, fn, ln, year):
        super().__init__(fn, ln)
        self.passyear = year

    def welcome(self):
        print("Welcome", self.fname, self.lname, "you have passed in year:", self.passyear)


x = Student("shiva", "prasad", 2017)
x.welcome()
x.printname()


class Rectangle:
    def __init__(self, lth, wth):
        self.length = lth
        self.width = wth

    def add(self):
        return self.length + self.width

    def multiply(self):
        return self.length * self.width


class Square(Rectangle):
    def __init__(self, lth,wth):
        super().__init__(lth, wth)


s = Square(20,10)
print('Addition:',s.add())
print('multiplication:',s.multiply())
