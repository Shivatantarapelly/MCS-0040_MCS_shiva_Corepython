'''
Python is an object oriented programming language.
Almost everything in Python is an object, with its properties and methods.
A Class is like an object constructor, or a "blueprint" for creating objects.
All classes have a function called __init__(), which is always executed when the class is being initiated.
for creating a class we use keyword "class"

class classname:
    method1():
    ----------
    method2():
    ---------
    .
    .
object = classname()  ---> creating object
object.methodname(parameters) ---> calling the method inside class

'''


class Shiva:
    def __init__(self, city):
        self.city = city

    def place(self):
        print('the city that shiva belongs to', self.city)


s = Shiva('hyderabad')
s.place()