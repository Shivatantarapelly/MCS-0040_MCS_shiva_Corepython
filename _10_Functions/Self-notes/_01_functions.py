# Functions
"""
A function is a block of organized, reusable code that is used to perform a single, related action.
 Functions provide better modularity for your application and a high degree of code reusing.

There are two types of functions
1. built in functions
2. user defined functions

Built in functions are like print(),int() etc which comes inbuilt with python and
but user defined function are those functions which we have to create for reusing the code by just simply
calling the function wherever it is required.

Function blocks begin with the keyword def followed by the function name and parentheses ( ( ) ).
Syntax: def function_name(parameters):
            ''function doc string''
            Business Logic
            return [expression]
"""

# example
# -------state-----
n1 = 10
n2 = 20


# ------behaviour----
# function definition
def add(a, b):  # function signature
    res = a + b  # function body
    print('sum of two no:', res)  # function body


add(n1, n2)  # function calling


# ------Function calling----

def diff(a, b):
    sub = a - b
    print("Difference if 2'nos:", sub)


diff(10, 20)  # calling directly by passing arguments as values
n1, n2 = 10, 20
diff(n1, n2)  # storing the values in variables and then using variables as arguments for calling the functions
diff(10 + 20, 20 + 30 * 2)  # passing expression as arguments for calling the functions
n1, n2 = 100 / 2, 2 * 5 + 3
diff(n1, n2)  # storing expression in a variable and using that variable as argument to call function


# ---- Arguments and parameters -------

def add_str(fn, ln):
    res = fn + ' ' + ln
    print("your name full name is:", res)


add_str('shiva', 'prasad')

'''
In above example the fn,ln are parameters whereas 'shiva' and 'prasad' are arguments.
so to call a function we need to pass arguments as parameters to a function. 
'''


# ---- Return type ------

def even_or_odd(n):
    if n % 2 == 0:
        return 'number is even'
    else:
        return 'number is odd'


even_or_odd(10)  # return whether the no. is even or odd but o/p is not displayed
print(even_or_odd(10))  # o/p can now display but we can use the return value only one time
re = even_or_odd(10)  # by storing it in another variable we can reuse the return value where ever req.
print(re)  # printing the o/p by using variable

"""
in the above example when value is returning only the address of location is returned so in print function 
the returned value is displayed then the value is removed from memory by garbage collector as there is no 
reference pointing to that address. if the returned value is stored in variable then the value can be used 
multiple times and value stores in memory until the variable pointing to that value address

"""
# ------ Different types in writing functions -------

"""
There are four types
* with return and with parameters
* without return and without parameters
* with return and without parameters
* without return and with parameters

"""


# with return and with parameters

def result(marks):
    if marks >= 35:
        return 'passed'
    else:
        return 'failed'


final_result = result(35)
print('you have: ', final_result)


# without return and without parameters

def intro():
    print('hi shiva')
    print('welcome')


intro()


# with return and without parameters

def price():
    print('the price of samsung mobiles are')
    return 10000, 15000, 20000


print(price())


# without return and with parameters

def course(n):
    if n == 'python' or n == 'java':
        print('yes the course is available')
    else:
        print('the course is not available')


course('python')

# ------- passing arguments ------

"""
1. Positional argument
2. default argument
3. keyword argument
4. Arbitrary argument
5. keyword Arbitrary argument
"""


# 1. Positional argument

def addition(a, b, c):
    d = a + b + c
    return d


s = addition(10, 20, 30)  # in positional argument a value is 10 and b is 20 and c is 30
print('sum is:', s)


# 2. default argument

def subtraction(a, b, c=10):
    d = a - b - c
    return d


s = subtraction(10, 20)  # in default case if arguments are not passed through the function call then it takes
print('Difference is:', s)  # default value
s = subtraction(10, 20, 30)  # in this case as argument is passed so it will take argument not default value
print('Difference is:', s)


# 3. keyword argument

def colour(r, b, w):
    print('r is : ', r)
    print('b is : ', b)
    print('w is : ', w)


colour('red', b='blue', w='white')  # in this red is pos argument , where b and w are keyword argument

# deep copy, shallow copy

lis1 = [10, 20, 30]
lis2 = lis1
print('both list are same:', lis1, lis2)
lis2[1] = 100  # changing 2nd index value of lis 2
print('now also both list are same:', lis1, lis1)  # changing in both list
# --- shallow copy -- 1st scenario
lis1 = [1, 2, 3]
lis2 = lis1.copy()
lis2[0] = 10  # changing the 0 index value of lis2
print('now both list will be different:', lis1, lis2)  # lis1 not change as it is shallow copy using copy()
# ---- 2nd scenario ---

lis1 = [[1, 2, 3], [10, 20, 30]]
lis2 = lis1.copy()
lis2[0][0] = 100
print('in this case shallow copy not works:', lis1, lis2)  # as it is referring to collection of item not object

# ---- Deep copy ----
import copy

lis1 = [[1, 2, 3], [10, 20, 30]]
lis2 = copy.deepcopy(lis1)
lis2[0][0] = 100
print('in this case the list will not change:', lis1, lis2)  # using deepcopy we cannot the copied list can only change
