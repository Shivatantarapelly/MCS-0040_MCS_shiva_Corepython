'''
3. assignment operators (+=,-=,*=, etc) updating or assigning the same value without duplicating the value again
'''
a = 10
print('operation1:',a)
a += 1
print('operation2:',a)
a %= 2
print('operation3:',a)
a -= 2
print('operation4:',a)
a /= 2
print('operation5:',a)
x = 22
x += (a*x)
print('operation6:',x)
s = 'shiva'
s += 'prasad'
print('operation7:',s)
# x -= s #TypeError: unsupported operand type(s) for -=: 'float' and 'str'
# s -= 'prasad'    #TypeError: unsupported operand type(s) for -=: 'str' and 'str'
# print('operation8:',s)
x /= a+10
print('operation9:',x)
a,b,c = 10,20,30
a /= b + (c**2)
print("operation10:", a)
a =10
a **= 2
print('operation11:',a)
a += True
print('operation12:',a)  #will add 1 to the result
a += False
print('operation13:',a) #nothing adds as value of false is 0
a *= True
print('operation14:',a) #will not change the value as true value is 1
a *= False
print('operation15:',a)  #will get 0 as the false value is 0 and anything *0 is 0
