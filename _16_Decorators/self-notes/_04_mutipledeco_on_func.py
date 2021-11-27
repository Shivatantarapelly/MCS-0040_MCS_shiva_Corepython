'''
we can use multiple decorators on a single function

'''


def upd(func):
    def inner():
        st = func()
        return st.upper()

    return inner


def splitdec(func):
    def wrap():
        st1 = func()
        return st1.split()

    return wrap


@splitdec
@upd
def newst():
    return 'hi shiva good morning'
'''
@upperd             this will  ot work as splitd func will first executes and coverts str to list
@splitd             after that it executes upd func but list has not method upper
def newst():
    return 'hi shiva good morning'
'''


print(newst())
