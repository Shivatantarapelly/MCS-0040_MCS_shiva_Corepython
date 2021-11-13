from abc import ABC, abstractmethod


class Company(ABC):  # inheriting abstract class
    @abstractmethod
    def calling(self):  # abstract method
        pass


class Airtel(Company):
    def calling(self):
        print('calling from Airtel company')


class Jio(Company):
    def calling(self):
        print('calling from Jio company')


'''
in above we are creating an abstract class with an abstract method but this method needs to be implemented
in respective sub class according to their requirement
'''


class System(ABC):

    @abstractmethod
    def config(self):
        pass


class Lenovo(System):
    def __init__(self, ram, color, memory):
        self.ram = ram
        self.color = color
        self.memory = memory


    def config(self):
        print('Ram :', self.ram)
        print('Memory :', self.memory)
        print('color:', self.color)


class Hp(System):
    def __init__(self, ram, color, memory):
        self.ram = ram
        self.color = color
        self.memory = memory

    def config(self):
        print('Ram :', self.ram)
        print('Memory :', self.memory)
        print('color:', self.color)


l = Lenovo(4, 'red', 64)
l.config()
h = Hp(6, 'silver', 128)
h.config()


