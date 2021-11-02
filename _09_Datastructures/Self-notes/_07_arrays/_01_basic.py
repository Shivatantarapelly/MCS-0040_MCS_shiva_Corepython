'''
An array is a collection of items stored at contiguous memory locations.
'''

'''
ARRAYS:
----------
 - Are used to store multiple values in single variable 
 - An array is a collection of items stored at contiguous memory locations.
'''

"""array = [1,10.89]
print("array      :",array)   # TypeError: integer argument expected, got float

"""

import array as ar

print("integer".center(40, "_"))
new = ar.array('i', [1, 2, 10, 16, 18, 100])  # create
print("new array :", new)  # retrieve

new_array = ar.array('d', [1, 2, 34, 5])  # create
print(new_array)  # retrieve

print("float".center(40, "_"))
new = ar.array('d', [1.9, 2.90, 10.17, 16.18, 18.17, 100.8])  # create
print("new array :", new)  # retrieve

print("index".center(40, '_'))

num = ar.array('i', [10, 14, 17, 19, 20])
print("numbers in array     :",num)
print("index of 0            :",num[0])
print("index of 1            :",num[1])
print("index of 2            :",num[2])
print("index of -1            :",num[-1])
print("index of -3            :",num[-3])

length_num = len(num)
i = 0
while length_num>0:
    print(f"index of {i-1} ".ljust(15, "_"), ":",num[i-1] )
    length_num-=1
    i-=1


for index, value in enumerate(num):
    print(f"index of {index} ".ljust(15, "-"),":",value)




print("update".center(40,'_'))
new_array.append(11)
print("updated array  :",new_array)
print("type of array  :",type(new_array))

"""
new_array.append(10)                      # take only exactly one argument
print("updated array   :",new_array)

new_array.append([10,11])           #TypeError: must be real  number, not list
print("updates array    :",new_array)   


new_array.append(10,11)
print("updates array    :",new_array)   ##TypeError: array.append() takes exactly one argument (2 given) """


print("changing the element".center(40,'_'))

num1 = ar.array('i',[10,11,17,18,19])

num1[0]=20
num1[1]=11

print("changing the value    :",num1)

