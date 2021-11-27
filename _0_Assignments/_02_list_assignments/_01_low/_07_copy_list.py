list1 = [10, 20, 30, 40]
list2 = list1
print(list2)
list2.remove(40)  # will remove 40 from both list1 and list2
print(list2)
print(list1)

# shallow copy

ls1 = [11, 22, 33]
ls2 = ls1.copy()  # .copy is used for shallow copy
print(ls2)
ls2.append(44)
print(ls2)
print(ls1)  # ls2 will change but ls1 will not change
ls1 = [1, 2, 3, [3, 4, 5]]
ls2 = ls1.copy()
ls2[3][0] = 4
print(ls1)
print(ls2)  # if there is list inside list shallow copy doesn't work and changes will reflects in both list

# deep copy

import copy

l1 = [1, 2, 3, [4, 5, 6]]
l2 = copy.deepcopy(l1)
l2[2] = 4
print(l2)
print(l1)
l2[3][0] = 5
print(l2)  # in this case deep copy will work the changes in one list will not affect in another list
print(l1)
