"""
# REQ:
           1. CRUD :  CREATE RETRIEVE UPDATE DELETE
           2. State (Datatype/structure)
           3. Behavior (Operators, DM, Loops) """

data = [1, 2, 10, 13, 16, 17, 19, 20, 22]  # create
print("normal data is                :", data)  # retrieve
data[0] = 123
print("updated data is               :", data)  # Update

del data[1]
print("after deleting updated data is:", data)  # delete

del data
print("after deleting                 :", data)

print("-------------------------list--------------------------")
num = [1, 2, 3, 4, 5]
print("list is                 :", num)
print("type of list            :", type(num))
print("id(address) of the list :", id(num))

'''List properties'''

'''
List properties:
==================
# 1. List will allow both homogeneous and heterogeneous data
# 2. List allows duplicate elements
# 3. Insertion order maintains
# 4. Follows indexing mechanism while storing elements
# 5. List is mutable*

'''

print("------ ----------------------1.List will allow both homogeneous and heterogeneous data-----------------------")
print("------------------------------------------------homogeneous---------------------------------------------------")
print("-------------------------integers---------------------------------")
num = [1, 2, 3, 4]
print("integers is list            :", num)

num1 = [1.1, 2.9, 3.98, 4.9]
print("floating numbers is list    :", num1)

str1 = ['kumar', 'kiran', 'shiva', 'yuvi']
print("strings is list             :", str1)

bool = [True, False, True, False]
print('boolean  is list            :', bool)

print('-------------list inside list----------------')
list = [1, 2, 3, 4, [8, 99, 10]]
print("list inside list            :", list)

list1 = [[1, 2, 3, 4], [5, 6, 7, 9], [10, 11, 12, 15]]
print("list inside list            :", list1)

print('------------list inside tuple----------------')
list_tup = [1, 2, 4, (10, 16, 18), (12, 19, 22)]
print("list inside tuple            :", list_tup)
list_tup1 = [(1, 2, 3, 4), (1, 2, 78), (19, 10, 18)]
print("list inside tuple            :", list_tup1)

print('----------list inside set--------------------')
list_set = [10, 20, 11, 33, {1, 2, 10, 18}]
print("list inside set               :", list_set)
list_set1 = [{1, 2, 3, 5, 7}, {10, 19, 11, 23}, {18, 16, 14, 12}]
print("list inside set                 :", list_set1)

print('--------list inside dictionary----------------')
list_dict = [1, 10, 19, 20, {'name': 'kumar', 'id': 27}]
print("list inside dictionary          :", list_dict)
list_dict1 = [{1: 'one', 2: 'two'}, {'name': 'kumar', 'loc': 'hyd'}]
print("list inside dictionary          :", list_dict1)

print("----------------------heterogeneous-----------------------------------------")
list_hetro = [1, 2, 3, 'kumar', ['yuvi', 'kiran', 'ram'], {1, 3, 5, 7, 8}, {'one': 1, "two": 2}]
print("heterogeneous list is           :", list_hetro)

print("------------------------ 2.List allows duplicate elements-------------------------------------")
list1 = [1, 2, 3, 4, 1, 10, 11, 16]
print("duplicate in list              :", list1)

print("------------------------3.Insertion order maintains------------------")
list2 = [1, 10, 11, 18, 12, 199]
print("insertion order in list        :", list2)

print("--------------------------- 4.list is mutable--------------------------")
list1 = [10, 12, 13, 1, 14, 7, 11]
#  0    1   2   3  4   5  6

print("Before list                     : ", list1)
list1[3] = 19
print("After list                      : ", list1)

print("-------------------------------5. Follow indexing mechanism-------------------------------")
list1 = [10, 12, 13, 1, 14, 7, 11]
print("0(zero)th index is              :", list1[0])
print('1st index is                    :', list1[1])
print('2nd index is                    :', list1[2])
print('-1 index is                     :', list1[-1])

#  0    1   2   3  4   5  6
