# differences

# print
"""
In python 2.x, “print” is treated as a statement and python 3.x explicitly treats “print” as a function.
This means we need to pass the items inside your print to the function parentheses in the standard way
otherwise you will get a syntax error.

"""

# print 'Hello, World!'   # in 2x
print('Hello, World!')  # in 3x

# integer division
"""
if you type the expression 3 / 2 in Python 2 code, the result of the evaluation will be 1, not 
1.5 as you might expect.
it is recommended to use either float(x) instead of using only x in your python 3 code
or use from __future__ import division in your python 2 scripts.
"""

print(3 / 2)  # in 2x it gives o/p int value as 2
print(3 / 2)  # in 3x it gives o/p exact float value 1.5

# we can achieve 3x feature in 2x by importing module from __future__ import division

# unicode

"""
python 3 stores strings in unicode format where as python 2 will store strings in ascii format

"""

# Raising exception

"""
Python 3 requires different syntax for raising exceptions. 
If you want to output an error message to the user, you need to use the syntax −
raise IOError(“your error message”)

the following code works only in python 2, not in python 3
raise IOError, “your error message”
"""

# list comprehension loop variables

# print 'Python', python_version()   o/p in version 2x  python 2.7.6
# i = 1
# print 'before: i =', i                                   i = 1
# print 'comprehension: ', [i for i in range(5)]           [0,1,2,3,4]
# print 'after: i =', i                                     i = 4
