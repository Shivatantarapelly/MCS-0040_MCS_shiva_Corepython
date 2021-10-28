# Displaying the details of pgs and prices when we call the method

class Pgs:
    def __init__(self, pg1, pr1, pg2, pr2, pg3, pr3):
        self.pg1 = pg1
        self.pr1 = pr1
        self.pg2 = pg2
        self.pr2 = pr2
        self.pg3 = pg3
        self.pr3 = pr3

    def details(self):
        print(f'the name of pg is: "{self.pg1}" and price is: {self.pr1}')
        print(f'the name of pg is: "{self.pg2}" and price is: {self.pr2}')
        print(f'the name of pg is: "{self.pg3}" and price is: {self.pr3}')


p = Pgs('luxury pg', 8000, 'sv pg', 5500, 'new gvs', 6000)
p.details()