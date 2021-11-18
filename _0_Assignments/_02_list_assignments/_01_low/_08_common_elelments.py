# Find common element from 2 lists

"""
CRUD : Retrieve
state : list
Behaviour: for, if, in
"""

# ---- algorithm -----

ls1 = [10, 25, 30, 50, 75, 80, 100]
ls2 = [15, 25, 35, 55, 75, 85, 95]
ls3 = []
ls1 = set(ls1)
ls2 = set(ls2)

for i in ls1:
    if i in ls2:
        ls3.append(i)
print('common elements in the from both list:', ls3)

lis1 = [10, 25, 30, 50, 75, 80, 100]
lis2 = [15, 25, 35, 55, 75, 85, 95]


# ---- function -----

def common_elements(l1, l2):
    l3 = []
    l1 = set(l1)
    l2 = set(l2)

    for i in l1:
        if i in l2:
            l3.append(i)
    print('common elements in the from both list:', l3)


common_elements(lis1, lis2)
