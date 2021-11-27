

class Emp:
    comp = 'MCS'
    loc = 'Bengaluru'

    def __init__(self, e1, e2, e3, s1, s2, s3, i1, i2, i3):
        self.e1 = e1
        self.i1 = i1
        self.s1 = s1
        self.e2 = e2
        self.i2 = i2
        self.s2 = s2
        self.e3 = e3
        self.i3 = i3
        self.s3 = s3

    def emp1_details(self):
        print(f'EMP ID : {self.i1}')
        print(f'EMP NAME : {self.e1}')
        print(f'EMP SALARY : {self.s1}')

    def emp2_details(self):
        print(f'EMP ID : {self.i2}')
        print(f'EMP NAME : {self.e2}')
        print(f'EMP SALARY : {self.s2}')

    def emp3_details(self):
        print(f'EMP ID : {self.i3}')
        print(f'EMP NAME : {self.e3}')
        print(f'EMP SALARY : {self.s3}')

    @classmethod
    def emp_detail(cls):
        print(f'EMP COMPANY: {Emp.comp}')
        print(f'COMPANY LOCATION: {Emp.loc}')


E = Emp('shiva', 'kumar', 'satish', 20000, 25000, 30000, 40, 27, 30)
E.emp3_details()
Emp.emp_detail()  # we can call the cls method both with class name reference as well as (this is preferable)
# ----- Or -----
E.emp1_details()  # like this object reference


'''
class Sample:
    def __init__(shiva, i, j):  # we can use any parameter instead of self but not preferable
        shiva.i = i
        shiva.j = j


    def s1(shiva):
        print(shiva.i)
        print(shiva.j)


    @staticmethod
    def s2():
        print('hi')

s = Sample(10,20)
s.s1()
Sample.s2()
'''