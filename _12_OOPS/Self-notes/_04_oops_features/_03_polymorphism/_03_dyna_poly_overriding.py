'''
overriding is an example for run time polymorphism or dynamic polymorphism
the concept is when we want to define a method in subclass which is already present in super class but we want
to implement our own behaviour using the same method signature or method name that is present in super class
then we can do that by overriding the method that is present in the super class.

so, method overriding is the concept of using the method signature of super class into our sub class but the changing
or overriding the behaviour of super class according to our needs.
'''


# without overiding

Even = []
Odd = []


class Even_Odd:

    def __init__(self, s, e):
        self.s = s
        self.e = e

    def even_odd(self):
        for i in range(self.s, self.e + 1):
            if i % 2 == 0:
                Even.append(i)
            else:
                Odd.append(i)
        print('even numbers:',Even)
        print('odd numbers:',Odd)


class Ev(Even_Odd):
    pass

ev = Ev(10,20)
ev.even_odd()       # by inheritance using both the method signature and behaviour in sub class

# method overiding

class Even_Odd:

    def __init__(self, s, e):
        self.s = s
        self.e = e

    def even_odd(self):
        for i in range(self.s, self.e + 1):
            if i % 2 == 0:
                Even.append(i)
            else:
                Odd.append(i)
        print('even numbers:',Even)
        print('odd numbers:',Odd)


class Ev(Even_Odd):
    def even_odd(self):        # overriding the method by implementing the behaviour
        for i in range(self.s, self.e + 1):
            if i % 2 == 0:
                Even.append(i)
        print('even numbers:', Even)

e = Ev(10,20)
e.even_odd()



