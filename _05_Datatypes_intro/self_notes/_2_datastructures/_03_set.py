#Set:
'''
Sets are again a collection of elements. But the difference from the above two is that sets
 do not hold duplicate values and the elements are not ordered. So, we cannot use indexing here.
 The elements get automatically arranged in ascending order when all values are int or float type.
'''
'''
1. add(): To add an element to a set.
2. pop():To remove the last element if index is not specified and if specified removes elements at that index.
3. clear(): To delete all the elements of a set.
4. len(): To find the length of a set, etc.
5. remove(): This removes the specified element from the set. This function gives an error if the element is 
   not present in the set.
6. discard(): This removes the specified element from the set. But this function does not give an error if the 
   element is not present in the set.
'''

s = {1,'shiva',10,'apple','sri',5,4.5}
print(s)
s.add(3)
print(s)
s.pop()
print(s)
s.remove('shiva')
print(s)
s.discard(10)
print(s)

'''
a. The union() returns the combined values from both the sets. And if any value is matched, 
   then it is returned only once.
b. The intersection() returns the set of common values from both the sets. If no common ones, 
   it returns an empty set.
c. The difference() function returns the set of values of the first set that are not there in the second one.
d. The symmetric_difference() returns the set of values from both the sets that are not common to the sets.
'''

a = {1,'sai',10,12.5,'sri'}
b =  {10,'shiva','sai',16,25}
print(a.intersection(b))
print(a.union(b))
print(b.difference(a))
print(a.symmetric_difference(b))