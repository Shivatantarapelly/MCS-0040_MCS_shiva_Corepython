
# Multiply of elements

"""
CRUD : create
state : list
behaviour : for, *=

"""

# ----- algorithm ------

li = [1, 2, 3]
res = 1
for i in li:
    res *= i

print(res)

li = [10, 20, 30]

# ------ function ------

def mul(lst):
    result = 1
    for j in lst:
        result *= j

    return result


print(mul(li))
