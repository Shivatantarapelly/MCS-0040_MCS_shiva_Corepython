# Remove specified index from list and print
"""
CRUD : Update
state: list
Behaviour : for, ==

"""

# ---- builtin -----

ls = [10, 20, 30, 40, 50]
x = int(input('enter the index number of element you want to remove:'))
del ls[x]
print(ls)

ls = [1, 2, 3, 4, 5]
x = int(input('enter the index number of element you want to remove:'))
ls.pop(x)
print(ls)

# ---- algorithm -----

lis = [11, 22, 33, 44, 55]
nlis1 = []

idx = int(input('enter the index number of element you want to remove:'))
for i in range(len(lis)):
    if i == idx:
        pass
    else:
        nlis1.append(lis[i])
print(nlis1)

# ----- function -----

lis = [111, 222, 333, 444, 555]


def remove_index(l):
    nl1 = []

    indx = int(input('enter the index number of element you want to remove:'))
    for j in range(len(l)):
        if j == indx:
            pass
        else:
            nl1.append(l[j])
    print(nl1)


remove_index(lis)
