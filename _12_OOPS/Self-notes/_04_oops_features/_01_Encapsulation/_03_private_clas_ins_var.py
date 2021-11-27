class A:
    __a = 10
    __b = 10


a = A
print(a._A__a * a._A__b)  # accessing private class variables out side class by using object._classname__class variable


class A:
    def __init__(self, a, b):
        self.__a = a
        self.__b = b


a = A(10, 10)
print(a._A__a + a._A__b)  # accessing the instance variable same as above


class A:
    def diff(self, a, b):
        self.__a = a
        self.__b = b


a = A()
a.diff(20,10)
print(a._A__a - a._A__b)  # accessing the instance variable same as above

