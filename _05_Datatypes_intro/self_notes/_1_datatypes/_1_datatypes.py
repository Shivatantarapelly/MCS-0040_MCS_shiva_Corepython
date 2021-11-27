#variables can be stored in different types and different types can do different things
#in python there is no need of declaring type of variable explcitly
# hence python is a dynamically typed language
#Every thing in python is an object
'''
1. text type: str
2. numeric types: int, float complex
3. sequence type: list, tuple, range
4. mapping type: dictionary
5. Set type: set, frozenset
6. boolean type: bool
7. binary type: bytes,bytearray, memory view
'''
#the data types are set when we assign as below
a = frozenset({1,2,'apple'})
b = b"12,hello"
c = bytearray(12)
d = [10,20,'hello']
print(type(b))    #by using type fuction we get type of variable
print(type(a))
print(type(c))
print(type(d))
#we can specify any data type as below
x = dict(name = 'shiva', age=26)
y = tuple((1,2,'shiva',15.36))
z = list((1,6,'prasad',12.5))
print(z)
print(y)
print(x)

#int
'''
int or integer is a whole number, +ve or -ve without any decimals of unlimited length
in python2, for long number i.e 13543688339 the type is long int but in python3 how long may be the number it is int
'''
x = 10
print('integer1:',type(x))
x = -12
print('integer2:',type(x))
x= 0
print('integer3:',type(x))

#float:
'''
Float is a number i.e +ve or -ve containing one or more decimal points
Float can also be scientific numbers with an "e" to indicate the power of 10.
'''
x= 12.5
print('float1:',type(x))
x= -12.5
print('float2:',type(x))
x= 0.0
print('float2:',type(x))

#Complex
'''
Complex numbers are written with a "j" as the imaginary part eg 5j, 9+5j etc
'''
x = 5j
print('complex1:',type(x)) #complex
x = 4+5j
print('complex2:',type(x))  #complex
x = 0+0j
print('complex3:',type(x))  #complex

# String:
'''
String in python can be declared by single or double quotation eg (a = 'shiva' or a = "shiva")
multiple line string can be assigned to a variable by using three quotes 
python doesn't have character data type, even a single character is a string
'''
x = 'm'
print('string1:',type(x))   #string
x = "shiva"
print('string2:',type(x))  #string
x = '123'
print('string3:',type(x))  #string
x = 'True'
print('string4:',type(x))  #string
x = '3+5j'
print('string5:',type(x))  #string


# Boolean
'''
In python we can evaluate an expression to get the value as true or False
we can also declare a bool type as below
'''
x = bool(15)
y = bool('shiva')
print(x)   #we get o/p as true unless value is 0, empty string or empty list etc
print(y)
x = bool(0)
y = bool('')
print(x)
print(y)



