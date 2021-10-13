#variables
'''
1. variables are containers for storing the data values.
2. Variables do not ne declared with any particular type and can even change type after they have been set.
3. you can get the type of the variable by using type function
4. string variables are declared either by using single or double quotes
5. a variable name must start with a letter or underscore character but can't start with a number.
6. Variable names are case sensitive.
7. Python allows you to assign values to multiple variables in one line
8. we can same value to multiple variables.
9. there are different types of variable such as global, local, output, instance ,class

'''

#interning
'''
for each variable memory will be stored in differnt memory location. each variable refers to an object and object holds
adress of the current variable but there is tecnique called iterning where if the values are same
 the python will alocate only one memory for different variable.
'''
#eg:
import sys
a = 10
b = 10
print(id(a),id(b)) #gives same address
a = a+1
print(id(a),id(b)) #gives diiferent address
a = 'hello'
b = 'hello world'
print(id(a),id(b)) #gives diiferent address
a = sys.intern(b)  #manually allocating same memory using intern method
print(id(a),id(b))
