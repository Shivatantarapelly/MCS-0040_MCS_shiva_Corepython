'''
Abstraction:
Abstraction in Python is the process of hiding the real implementation of an
application from the user and emphasizing only on usage of it.
example is, when you use TV remote, you do not know how pressing a key in the
remote changes the channel internally on the TV. You just know that pressing +
volume key will increase the volume.
Through the process of abstraction in Python, a programmer can hide all the irrelevant
data/process of an application in order to reduce complexity and increase efficiency.
'''

'''
In Python, abstraction can be achieved by using abstract classes and methods in our programs.
A class containing one or more abstract methods is called an abstract class.
Abstract methods do not contain any implementation. Instead, all the implementations can be 
defined in the methods of sub-classes that inherit the abstract class. An abstract class is created 
by importing a class named 'ABC' from the 'abc' module and inheriting the 'ABC' class.

syntax:
#first importing the abstract class module and abstract method
from abc import ABC,abstract method
class class_name(ABC):
    @abstract method
    def method_name(self):
        pass
we can't call this method or can't create object directly instead we have to create another class
and method with same abstract method name and can create object for that class and call that method.
'''



