# Remove duplicates
"""
CRUD : update
state : list
behaviour : for, in, not in

"""
# ------ algorithm ------

lis = [10, 20, 30, 25, 10, 23, 10, 25, 45, 63]
s = set(lis)
nlis = list(s)
print(nlis)

ls = [10, 20, 30, 25, 10, 23, 10, 25, 45, 63]
nls = []
for i in ls:
    if i not in nls:
        nls.append(i)
print(nls)

# ------ function -------

ls1 = [10, 20, 30, 25, 10, 23, 10, 25, 45, 63]
nls1 = []


def rem_duplicate(lis1, nlis1):
    for k in lis1:
        if k not in nlis1:
            nlis1.append(k)
    print(nlis1)


rem_duplicate(ls1, nls1)



