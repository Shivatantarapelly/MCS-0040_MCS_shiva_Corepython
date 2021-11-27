# showing the prices of the courses when the method is called

class Courses:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def price(self):
        print('the price of python course is:', self.x)
        print('the price of java course is:', self.y)
        print('the price of dot net course is:', self.z)


C = Courses(25000, 30000, 20000)
C.price()
print(C.x)