#Data structures
'''
Data structures can organize and stores the data in an efficient manner so that we can modify and access
the data in the future.
Built in data structures are list, tuple, set ,dictionary\
'''
# List:
'''
List are containers of values of different data types.These store the data in a continuous manner in the 
memory. These are mainly used in situations where there is a need to access the data frequently, which 
can be done easily using indexing.
1. append(): This function is used to add an element to the list at the end.
2. insert(): This function takes the element and the index as arguments and inserts the value in the 
             specified location.
3. pop(): This function deletes the last element if no index passes or deletes the element at that 
          index and returns it.
4. remove(): This function removes the specified value from the list.
5. len(): This function returns the length or number of elements in the list
6. sort(): This arranges the elements of the list in ascending or descending order
7. index(): This is used to find the index of the element passed
8. count(): This finds the number of times the value occurs in a list
'''
a = ['shiva',10.5,2,45]
print(a)
a.pop(1)   #the index no should be passed
print(a)
a.insert(1,'sai') # passing index then value
a.insert(2,20) # passing index then value
print(a)
a.remove('sai')
a.remove('shiva')
print(a)
a.sort()
print(a)
a.sort(reverse=True)
print(a)
a.extend([1,2])
print(a)
print(a.index(20))
a.extend([1,'shiva'])
print(a)
a.clear()
print(a)
x= ['sai','shiva',2,10]
for i in enumerate(x,start=1):
    print(i)
l = ['shiva','apple',10,25.5,12]
print('list ops1:',l[0])
l1 = [10,20,'sai',[1,2,3],{1,2,3},(1,2,3),{'a': 'apple','b':'ball'}]
print('accesing tuple:',l1[5])
print('acessing set:',l1[4])
print('accessing dict values:',l1[6]['a'])
l3 =[10,[1,2,[10,20,30],[12,14,16]],[7,8,9]]
print('nestedlist ops1:',l3[1][2][1]) #20
print('nestedlist ops1:',l3[1][3][2]) #16
