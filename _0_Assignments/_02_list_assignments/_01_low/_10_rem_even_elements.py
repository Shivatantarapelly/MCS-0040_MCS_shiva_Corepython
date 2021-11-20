# Remove even elements and print list

"""
CRUD : update
state: list
Behaviour : for, ==
"""

# ----- Algorithm ------

lis = [10, 20, 30, 40, 50, 60]
nlis = []

for i in range(len(lis)):
    if i % 2 == 0:
        nlis.append(lis[i])
print(nlis)

# ---- function ----

li = [10, 20, 30, 40, 50, 60]


def rem_even_elements(lis):
    nlis = []

    for i in range(len(lis)):
        if i % 2 == 0:
            nlis.append(lis[i])
    print(nlis)


rem_even_elements(li)
