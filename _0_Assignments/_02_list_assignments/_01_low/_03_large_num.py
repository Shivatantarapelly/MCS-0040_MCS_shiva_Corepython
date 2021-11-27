# Largest number from list

"""
CRUD : retrieve
state : list
behaviour : for, < , =

"""

# ----- built - in ------

li = [10, 25, 36, 2, 43, 89, 26, 36]
li.sort()
print('largest number in the list:', li[-1])

# ----- algorithm ------

li = [10, 12, 35, 12, 100, 78, 103, 25, 36]
for i in range(len(li)):
    for j in range(len(li)):
        if li[i] < li[j]:
            li[i], li[j] = li[j], li[i]

print('largest number in the list:', li[-1])
print(li)

# ---- function -----

ls = [10, 12, 35, 12, 100, 78, 103, 25, 36]


def large_num(li):
    for i in range(len(li)):
        for j in range(len(li)):
            if li[i] < li[j]:
                li[i], li[j] = li[j], li[i]

    print('largest number in the list:', li[-1])
    print(li)


large_num(ls)

