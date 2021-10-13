'''
1. Airthmetic operators: (+,-,/,*,//,**,%)
'''
a = 10
b = 2
print(10+10)
c = a*b/b
print('multiplication1: ',a*b)
print('Result1: ',c)
print('sum1: ',a+b+c)
print('difference1:', a-b)
print('division1:',a/b/c)
print('floordivision1:',a//b)
print('modulus1:',a%b)
print('power1',a**b)
print('addition2:',c + 100)

x = 12.5
y = 25
z = 'shiva'
# print(x+z) #TypeError: unsupported operand type(s) for +: 'float' and 'str'
print(x+y)
c = x*(x/y)
print('result:',c)
print('operation1:',c+(c**2))
print('operation2:',c-(c/y))
print('operation3:',c*(x+y)/c)
print('operation4:',True * False) #value is 0
print('operation5:',True + False) #value  is 1
# print('operation6:',True % False) #ZeroDivisionError: integer division or modulo by zero
print('operation7:',False/True) #Value is 0.0
print('operation8:',c + True) #adds one to the result
# print('operation9:',c%False)  #ZeroDivisionError: float modulo
d = c/c
if True:         #here true value is 1
    print(True)

f = 10 * (a/b) + c *(a+b)
print('Result:', f)
print('operation10:',f%10)
