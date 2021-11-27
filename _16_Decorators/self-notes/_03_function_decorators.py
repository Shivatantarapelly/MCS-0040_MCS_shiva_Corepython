# without decorator

def outer(func):
    def inner():
        st = func()
        return st.upper()

    return inner


def string():
    return 'hi shiva'


data = outer(string)
print(data())


# with decorator

@outer
def newstr():
    return 'Good Morning'


print(newstr())


# Using decorator function for handling exception as below

def outer(func):
    def inner(x, y):
        if y == 0:
            return 'give valid input'
        else:
            return x / y

    return inner


@outer
def div(a, b):
    return a / b


print(div(2, 2))



'''
Decorator:
need to take a function as parameter
add functionality to the function
function needs to return another function

'''
