'''
Polymorphism:
Polymorphism means multiple forms.
In python we can find the same operator or function taking multiple forms.
It also useful in creating different classes which will have class methods with same name.
That helps in re using a lot of code and decreases code complexity.
In simple words, polymorphism allows us to perform the same action in many different ways.

Using method overriding polymorphism allows us to defines methods in the child class that have
the same name as the methods in the parent class. This process of re-implementing the inherited
method in the child class is known as Method Overriding.

In polymorphism, Python first checks the object’s class type and executes the appropriate method when
we call the method

'''


class Vehicle:

    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price

    def show(self):
        print(f'Details: car name: {self.name}, car colour: {self.color}, car price:{self.price}')

    def max_speed(self):
        print('Vehicle max speed is 150')

    def change_gear(self):
        print('Vehicle change 6 gear')


class Car(Vehicle):
    def max_speed(self):
        print('Car max speed is 240')

    def change_gear(self):
        print('Car change 7 gear')


c = Car('swift', 'red', 100000)
c.show()
c.max_speed()
v = Vehicle('swift', 'red', 100000)
v.show()
v.max_speed()
v.change_gear()


'''
Static polymorphism (compile time ) method overloading
dynamic polymorphism (run time) method overriding


'''