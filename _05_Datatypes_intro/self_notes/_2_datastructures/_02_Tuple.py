#tuples
'''
A tuple is also a collection of elements of different data types.
The difference between a tuple and a list is that lists are mutable whereas tuples are not.
'''
a = (1,2,3)
print(a[1])
'''
Tuples do not allow you to change or delete a particular element of a tuple. When we try adding/deleting
 an element, we get an error.
'''
a = 2,5,6
print(a) #the o/p will be given as tuple and assigning variables like these is called as packing
b,c,d = a   #we can assign values of the tupless to diffenent variables
print(b)     #this type of assigning values is called unpacking
print(c)
print(d)


tup1 = (10,20,30,[20,30,40],{10,20,30})
print('accessing list1:',tup1[3])
print('accessing se1:',tup1[4])

