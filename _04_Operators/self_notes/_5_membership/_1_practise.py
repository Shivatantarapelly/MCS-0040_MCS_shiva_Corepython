
'''5. membership operators (in,not in)
'''
l1= [1,2,3,4,5,6]
l2 = [10,20,'shiva',25.5,'prasad']
print('1:',10 in l2) #true
print('2:','shiva' not in l2) #false
print('3:', l1 in l2) #false
print('4:',l1 not in l2) #true
print('5:', 2,5,6 in l1) # result 2 5 True
l1 = (1,2,3)
l2 = (1,4,2,5,3)
print('6:',l1 in l2) #false
l2 = (4,5,(1,2,3))
print('7:', l1 in l2) #true
d = dict((['a','apple'],['b','ball'],['c','cat']))
print(d)
print('8:', 'a' in d) #true
print('9:','cat' in d) #false
print('10:','cat' in d.values()) #true
print('11:','c' not in d.values()) #true
