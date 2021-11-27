# displaying the employee details when the method is called

class Emp:
    def __init__(self, name, id, desgnation, salary):
        self.name = name
        self.id = id
        self.designation = desgnation
        self.salary = salary

    def details(self):
        print(f'Employee name: {self.name}')
        print(f'Employee Id: {self.id}')
        print(f'Employee Designation: {self.designation}')
        print(f'Employee Salary: {self.salary}')


E = Emp('Shiva', 123, 'Software developer', 50000)
E.details()