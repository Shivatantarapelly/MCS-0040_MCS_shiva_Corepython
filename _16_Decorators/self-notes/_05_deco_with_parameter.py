'''
we can pass parameter to a decorator as below
'''


def outer(x):
    def upd(func):
        def inner():
            return func() + x

        return inner

    return upd


@outer(' shiva')  # passing parameter to decorator
def msg():
    return 'Good Morning'


print(msg())

'''
we can use same decorator on different functions
'''


def outer1(func):
    def inner(*args):
        lst = []
        lst = args[1:]
        for i in lst:
            if i == 0:
                return "give proper input"
        return func(*args)

    return inner


@outer1
def div1(a, b):
    return a / b


@outer1
def div2(a, b, c):
    return a / b / c


print(div1(2, 2))  # O/P : 1
print(div1(2, 0))  # o/p : give proper input
print(div2(4, 2, 2))  # O/P : 1
print(div2(4, 0, 2))  # o/p : give proper input

print(div2.__name__)  # it gives name as inner but the function call is div2. due to decorator it hides

# to get the actual function name then we have to do it as below by importing func tools

import functools


def outer(func):
    @functools.wraps(func)
    def inner():
        st = func()
        return st.upper()

    return inner


@outer
def div():
    return 'shiva'


print(div())
print(div.__name__)  # now the o/p will be div





