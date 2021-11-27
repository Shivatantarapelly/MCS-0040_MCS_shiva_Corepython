'''
4.logical operator(and, or, not)
used for validating two expression with relational operators
'''

a,b,c = 20,20,65
if a>= 35 and b>=35 and c>=35:
    print('you are passed')
elif a<35 and b<35 and c<35:
    print('you are failed in all ')
elif a>=35 and b>=35 and c<35:
    print("you must skip 'c' to get pass ")
elif a<35 and b>=35 and c>= 35:
    print("you must skip 'a' to get pass ")
elif a>=35 and b<35 and c>=35:
    print("you must skip 'b' to get pass")
else:
    print('you failed in 2 subjects')

print('operation1:',a>b and b>c) #false
print('operation2:',a>b and b>c or a<c)   #true
print('operation3:',a == b and b == c or c>b)#true
x = 'shiva'
print('operation4:',a == x or b == x or c == x) #false
print('operation5:',a != x or b == x or c == x) #true
y = 'prasad'
print('operation6:',x==y) #false
print('operation7:',x>y)#true as per ascii numbers
print('operation8:',x == y or x>y) #true
# print('operation9:',x >y and x> a) #TypeError: '>' not supported between instances of 'str' and 'int'
print('operation10:',x == True or y == True) #false as both are false
print('operation11:',x != y and a == b and c<b or a<b or c>a) #true





