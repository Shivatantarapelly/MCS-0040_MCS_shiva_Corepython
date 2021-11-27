# get the employees of an organisation details

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
        print(f'EMP COMPANY: {Emp.comp}')
        print(f'COMPANY LOCATION: {Emp.loc}')

    def emp2_details(self):
        print(f'EMP ID : {self.i2}')
        print(f'EMP NAME : {self.e2}')
        print(f'EMP SALARY : {self.s2}')
        print(f'EMP COMPANY: {Emp.comp}')
        print(f'COMPANY LOCATION: {Emp.loc}')

    def emp3_details(self):
        print(f'EMP ID : {self.i3}')
        print(f'EMP NAME : {self.e3}')
        print(f'EMP SALARY : {self.s3}')
        print(f'EMP COMPANY: {Emp.comp}')
        print(f'COMPANY LOCATION: {Emp.loc}')


E = Emp('shiva', 'kumar', 'satish', 20000, 25000, 30000, 40, 27, 30)
E.emp1_details()  # this is preferable
# ----- or -------
Emp('shiva', 'kumar', 'satish', 20000, 25000, 30000, 40, 27, 30).emp3_details()
# ----- or ------
Emp.emp1_details(E)
