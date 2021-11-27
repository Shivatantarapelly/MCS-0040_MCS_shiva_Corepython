'''
# for loop syntax
        for <var> in <sequence>:
           # statements
A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
'''
'''
#printing number present in the list
l = [1,2,3]
for i in l:
    print(i)  #o/p 1 2 3

print('-------------------')

#Printing string's present in list

l = ['apple','banana','mango']
for i in l:
    print(i)

print('--------------------')

#Printing the min number present in the list

num = [10,25,6,20,40]
res = num[0]
for i in range(1,len(num)):
    for j in num:
        if num[i] < j:
            if num[i] < res:
                res = num[i]
print(res)
print('-----------------')

#printing 1 to 100 number

for i in range(1,101):
    print(i,end=' ')

print('-----------------------')

#iterating the string using for loop
s = 'shiva prasad'
for i in s:
    print(i,end=' ')

print('')
print('-----------------')

s = {'a': 'apple', 'b': 'ball', 'c': 'cat'}
for i in s:
    print(i, ':',s[i])

print('-----or-----')

for key in s:
    print(key)

print('-------or-------')

for key in s.keys():
    print(key)

print('----------------------')

for value in s.values():
    print(value)

print('-------------------')

for key,value in s.items():
    print(f'keys: {key} : value: {value}')

print('----------------')

l= [10,20,30,40]
for i in range(len(l)):
    print('values in list are:',l[i])
'''

#taking user input and printing the list of odd number and even numbers
'''
user = int(input('enter a number:'))
if user > 0:
    l1 = []
    l2 = []
    for i in range(1,user+1):
        if i%2 == 0:
            l1.append(i)
        else:
            l2.append(i)
    print('----even numbers-----')
    for i in l1:
        print(i,end=' ')
    print('')
    print('-----oddnumbers----')
    for i in l2:
        print(i,end=' ')
else:
    print('enter valid number')
'''

#taking the user input and printing prime numbers

user = int(input('enter a number:'))
for i in range(2,user-1):
    if user%i == 0:
        isprime = False
        break
    else:
        isprime =True



