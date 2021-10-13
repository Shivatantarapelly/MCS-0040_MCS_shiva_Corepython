'''
2. relational operators( >=,==,<=,<,> etc) comparing l.h.s and r.h.s
'''
a = 2
if a >= 2:
    print('greater')
elif a < 2:
    print('lesser')
else:
    print(a)
x = 10
y = 'shiva'
z = 12.5
u = True
print('operation1:',z==u)
print('operation2:',z!=u)
print('operation3:',z>=u)
# if z < y:    # TypeError: '<' not supported between instances of 'float' and 'str'
#     print(u)
print('operation4:',z==y)
c = x+z
d= 22.5
g = c/d
if g == True:       #result is true as g value is 1 and True value is 1
    print('operation5:',u)
else:
    print('operation5:',False)
if g > d:
    print('operation6:',g)
elif c>z:
    print('operation6:',c)
else:
    print(c)

print('operation7:',c>=c) #true
print('operation8:',c>c)  #false

