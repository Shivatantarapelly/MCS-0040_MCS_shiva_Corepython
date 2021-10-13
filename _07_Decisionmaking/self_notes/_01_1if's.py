'''
It is the prediction of conditions that occur while executing a program to specify actions.
if statement can predict true if condition result is true or non zero or non none and
predict false if condition result is false or zero or none
'''

if True:
    print('Success') # as condition is true it executes the if block statements

# if False:
#     print('unsucess') #the statement is not executed as condition is false
a = 2
b = 3
c = 1
if (a+c)-b: #result:0
    print('condition value is o:',a)    #statement not executed
if a-c+b: #result: 4
    print('condition value is 1:',a)    #statement exeuted
if a<b:
    print('b is greter')

if a>c:
    print('a is greater')

if a>=c and a is not b:
    print('and operation')
if a is True and b is True:  # false statement
    print('and with true')

if a == True and b == True:   #false statement
    print('and, assign, true')
if a == True or c == True:
    print('or ,asssign,bool')

# x = int(input('enter anumber: '))
# if 1:
#     print('you have entered:', x)
# if 0:
#     print('i have enterde:',x) #not executes

l = [1,2,3]
if l:
    print(l)
l.clear()
if l:
    print(l)

if {1,2,3}:
    print('sucess1')

# if {}:
#     print('sucess2')# not executes
n = 10
if n:
    print('sucess3')
n = ''
if n:
    print('sucess4') #not executes

if -17:
    print('sucess5')

if -17 and -2:
    print('sucess6')

if 15 or 0:
    print('sucess 7')
if 15 and 0:
    print('sucess8') #not executes
if not 0:
    print('sucess9')

if 15 and not 0:
    print('sucess10')
if False is 0:
    print('sucess11') #not executes
if False == 0:
    print('sucess12')

if True == 1:
    print('sucess13')
if True == 10:
    print('sucess14') #not executed

name = 'shiva'
if name == 'shiva' or 'SHIVA':
    print(name)
if len(name) == 5:
    print('length if str',len(name))

if name == 'SHIVA': #not executed
    print('Shiva')
