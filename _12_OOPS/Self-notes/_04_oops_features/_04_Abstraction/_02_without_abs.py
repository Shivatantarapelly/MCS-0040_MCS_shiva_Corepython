
class Company:
    def calling(self):
        print('---calling from the company----') #here this statement has no use as it is getting overriden in subclass
class Airtel(Company):
    def calling(self):
        print('calling from airtel company')   #here the behaviour is different but method signature is same

class Jio(Company):
    def calling(self):
        print('calling from jio company')

'''
so to avoid the useless code being written we use abstract method
when there is a requirement of using same method signature in all sub class but want a unique or different
behaviours in all sub classes then we use this abstraction.
'''