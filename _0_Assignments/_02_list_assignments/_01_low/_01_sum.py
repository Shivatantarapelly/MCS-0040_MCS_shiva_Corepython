# Sum of elements

"""
CRUD : create
state : list
behaviour : for, +=

"""

# ---- built in ----

l1 = [10, 20, 30]
l2 = sum(l1)
print(l2)

# ---- algorithm -----

l1 = [10, 20, 30]
res = 0
for i in l1:
    res += i
print(res)

# ---- function -----

l = [10, 20, 30]


def sum1(ls1):
    result = 0
    for j in ls1:
        result += j
    print(result)


sum1(l)
