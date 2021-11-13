'''
you can create a method that can be called in different ways. So, you can have a
 method that has zero, one or more number of parameters. Depending on the method definition,
 we can call it with zero, one or more arguments.

static polymorphism (compile time ) method overloading
we can create a method with specified number of parameters and calling that method in different ways by passing
different arguments.

'''

# without oveloading concept

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


eo = Even_Odd(2, 20)      # the method can be called only in one way
eo.even_odd()

# with overloading concept

Even = []
Odd = []


class Even_Odd:

    def __init__(self, s = 1, e = 20):
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


eo = Even_Odd()          # calling the method in different ways by passing different number of arguments
eo.even_odd()
eo = Even_Odd(2)
eo.even_odd()
eo = Even_Odd(2, 30)
eo.even_odd()
