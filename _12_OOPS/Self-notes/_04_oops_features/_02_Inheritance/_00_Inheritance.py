'''
Inheritance:
Inheritance allows us to define a class that inherits all the methods and properties from another class.
Parent class is the class being inherited from, also called base class or super class
Child class is the class that inherits from another class, also called derived class or subclass

class A:
    def __init__(self):
        state
    def function_name(self)
        behaviour
class B(A):
    def __init__(self):
        state
    def function_name(self):
        behaviour


Inheritance represents real-world relationships well, provides reusability & supports transitivity.
It offers faster development time, easier maintenance and easy to extend.

5 types of inheritance

Single
Multiple
Hierarchical
Multi-level
Hybrid

'''


# single inheritance

class Mobile:  # super class
    def __init__(self, model, price):
        self.model = model
        self.price = price


class Samsung(Mobile):  # sub class

    def sam_mob(self):
        print(f'the brand is {self.model} and price {self.price}')


t = Samsung('A30', 25000)
t.sam_mob()


# multilevel inheritance

class Mobiles:
    def __init__(self, p1, b1):
        self.p1 = p1
        self.b1 = b1


class Brand(Mobiles):
    def sam_mob(self):
        print(f'the Brand of mobile is: {self.b1}')


class Samsung(Brand):
    def price(self):
        print(f'the price of mobile is: {self.p1}')


s = Samsung(15000, 'samsung')
s.sam_mob()
s.price()


# Hierarchical inheritance


class Mobiles:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2


class Samsung(Mobiles):
    def sam_mob(self):
        print(f'the price of samsung mobile is: {self.p1}')


class Oppo(Mobiles):
    def oppo_mob(self):
        print(f'the price of Oppo mobile is: {self.p2}')


o = Oppo(15000, 20000)
o.oppo_mob()
s = Samsung(15000, 20000)
s.sam_mob()


# multiple inheritance

class Samsung:
    def __init__(self, p1):
        self.p1 = p1

    def sam_details(self):
        print(f'the price of samsung mobile is:{self.p1}')


class Oppo:
    def __init__(self, p1):
        self.p1 = p1

    def oppo_details(self):
        print(f'the price of oppo mobile is:{self.p1}')


class Mob(Samsung, Oppo):
    def __init__(self, p1):
        super().__init__(p1)
        print('the mobile details are below')


m = Mob(15000)
m.oppo_details()