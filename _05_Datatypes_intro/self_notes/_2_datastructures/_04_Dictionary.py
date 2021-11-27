# Dictionaries are data structures that store key-value pairs.
# These keys should be unique and cannot be changed
# We can access the elements of a dictionary using the keys

'''
1. get(): To get a value of the specified key.
2. pop(): Takes a key as an argument, deletes that key-value, and returns the value.
3. popitem(): Deletes the last key-value and returns the key-value pair as dictionary.
4. clear(): To delete all the elements of a dictionary. It keeps the instance of the dictionary,
   that is we can access the dictionary after clearing. It gives an empty dictionary.
5. keys(): Get all the keys in the dictionary.
6. values(): Get all the values in the dictionary.
7. items(): Get all the key-value pairs.
8. enumerate(): to get the index number of values in the dictionary
'''

d = {'a':'apple',1 :'ball','twenty': 20, 5:2.5}
print(d[1])  #accesing dictionary elements
d[1] = 'car' #changing the values using key
print(d)
d['alarm'] = 'clock' #adding key and value elements dictionary
print(d)
print(d.get('a')) #getting the values from dic using key
print(d.pop(5))   #should pass key as parameter to delete the pair
print(d)
x=d.popitem()   #will delete last pair from dic and can be returned as tuple with key,value as element in the tuple
print(type(x))  #type will be tuple
print(x)
print(d.keys())
print(d.values())
print(d.items())
x = {'a':'apple',1 :'ball','twenty': 20, 5:2.5}
for i,j in enumerate(x,start=1):
    print(i)

y = dict(sai=10,shiva=12,sri = 'prasad')
print(y)

num1 = dict([('x',5),['y',6]])
print(num1)
num2 = dict(dict(zip(['x','y','z'],{1,2,3})))
print(num2)

dic = {'a':10,'b':20,'c':30,'d':40}
print('accesiing values[b]:',dic['b'])
dic['e'] = 50
print('adding keyvalue :',dic)
del dic['b']
print('deleting keyvalue:',dic)
dic['c'] = 50
print('updating the value:', dic)
dic1 = {'apple':{'red':10, 'white':20, 'green':30},
        'mango':{'red':{'light':20,'dark':40},'orange':50, 'yellow': 60},
        'grapes':{'green': 50, 'black':60}}
print('accesing apple values:',dic1['apple'])
print('accesing mango values:',dic1['mango'])
print('accesing grape values:',dic1['grapes'])
print('accesing red mango values:',dic1['mango']['red'])
print('accesing light red mango values:',dic1['mango']['red']['light'])
print('accesing black grape values:',dic1['grapes']['black'])

