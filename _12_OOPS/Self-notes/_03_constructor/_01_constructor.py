'''
def __init__(self): this is called as a constructor as this will help us to create object.
self is a special parameter which is referred by object address where we can initialise
all instance variable.

class classname:
    def __init__(self):  ----> is called as default constructor as no parameters passing to init method
        pass

class classname:
    pass    ---> even in this scenario python will execute as imaging
                           class classname:
                                def __init__(self):   ---> as it is a default constructor
                                    pass

-----another scenario-----

class classname:
    def __init__(self,parameter 1,parameter2,...)  ---> parameterised constructor
        pass

therefore, init method with no parameters except self then it is called as default constructor and
init method with parameters is called as parameterised constructor

so, there are two types of constructor
default constructor
parameterized constructor ---> positional arguments
                               default arguments
                               keyword arguments
'''


# using default constructor
class Book:
    def __init__(self):  # default constructor
        pass

    def python(self, price, pages):
        print(f'price of book{price},and no of pages{pages}')


b = Book()
b.python(5000, 360)


# using parametrised constructor

class Book:
    def __init__(self, price, pages):  # parameterised constructor
        self.price = price
        self.pages = pages

    def python(self):
        print(f'price of book{self.price},and no of pages{self.pages}')


b = Book(5000, 360)
b.python()
