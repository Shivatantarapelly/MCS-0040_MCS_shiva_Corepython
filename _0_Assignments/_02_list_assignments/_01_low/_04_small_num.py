# Smallest number from list

"""
CRUD : retrieve
state : list
behaviour : for, < , =

"""

li = [10, 25, 36, 2, 43, 89, 26, 36]
li.sort()
print('largest number in the list:', li[0])

# ----- algorithm ------

li = [10, 12, 35, 12, 100, 3, 78, 103, 25, 36]
for i in range(len(li)):
    for j in range(len(li)):
        if li[i] < li[j]:
            li[i], li[j] = li[j], li[i]

print('largest number in the list:', li[0])
print(li)

# ---- function -----

lis = [23, 56, 42, 12, 1, 56, 14, 75, 23, 6, 2]


def large_num(ls):
    for idx1 in range(len(ls)):
        for idx in range(len(ls)):
            if ls[idx1] < ls[idx]:
                ls[idx1], ls[idx] = ls[idx], ls[idx1]

    print('largest number in the list:', ls[0])
    print(ls)


large_num(lis)
