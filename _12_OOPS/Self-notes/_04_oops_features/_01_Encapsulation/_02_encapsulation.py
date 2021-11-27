'''
Encapsulation:
Encapsulation in Python is the process of wrapping up variables and methods into a single entity.
In programming, a class is an example that wraps all the variables and methods defined inside it.
In Python, Encapsulation can be achieved using Private and Protected Access Members.
Private variables are preceded by using two underscores.
Protected variables are preceded by using a single underscore.

'''


class Person:
    def __init__(self, name, age, course):
        self.__name = name
        self.__age = age  # __age represent private variable
        self._course = course  # _course represent protected variable

    def display(self):
        print(self.__name)
        print(self.__age)
        print(self._course)


p = Person('shiva', 26, 'python')
p.display()
print(p._course)  # we can access protected variable outside the class
p._course = 'java'  # we can change the value of protected variable outside the class
# p.--name = 'sai'     # private variables cannot be modified
# print(p.__name)       # neither accessed out of class
p.display()

'''
in the same way private methods can be accessed and modified only inside the class and protected method
can be accesed inside and outside class
if you want to access and modify private variables we can achieve in below way
'''


class Person:
    def __init__(self, name, age, gender):
        self.__name = name
        self.__age = age  # declaring private variable
        self.__gender = gender

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value


p = Person('shiva', 26, 'male')
print(p.name)         # accessing the private varible outside class
p.name = 'sai'        # modifying the private variables outside class
print(p.name)