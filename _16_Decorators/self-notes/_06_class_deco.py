'''
we can use decorators function on methods inside the class as below
'''


def outer(func):
    def inner(ref):  # here we can take any name as like ref or self or anything
        if ref.name == 'shiva':
            print('matched the name')
        else:
            func(ref)

    return inner


class Name:
    def __init__(self, name):
        self.name = name

    @outer
    def msg(self):
        print('the name you entered is:', self.name)


n = Name('shiva')
n.msg()  # o/p : matched the name
N = Name('sai')
N.msg()  # o/p" the name you entered is sai

a = Name('shiva')
# a()    # it shows error as not callable when we call like this as there is no call method


'''
__call__ method:
after creating the object for the class we cannot call method inside class without method name by just object()
in this case we can use call method so that there is no need of method name reference and can execute the code
inside the call method by just object()
'''


class Name:
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('the name you entered is:', self.name)


A = Name('shiva')
A()  # as now we have call method the statement inside that method will execute

'''
using class as decorator and using on a function
'''


class Check_div:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        lst = args[1:]
        for i in lst:
            if i == 0:
                return 'you cant divide change the input'
            else:
                return self.func(*args, **kwargs)


@Check_div
def div(x, y):
    return x / y


print(div(2, 2))
print(div(2, 0, 5))
