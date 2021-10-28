
# displaying the prices of movie theater when the method is called

class Mov_price:
    def __init__(self, lc, pr1, dc, pr2, bc, pr3):
        self.lc = lc
        self.pr1 = pr1
        self.dc = dc
        self.pr2 = pr2
        self.bc = bc
        self.pr3 = pr3

    def price(self):
        print(f'the name of network is: "{self.lc}" and price is:Rs {self.pr1}')
        print(f'the name of network is: "{self.dc}" and price is:Rs {self.pr2}')
        print(f'the name of network is: "{self.bc}" and price is:Rs {self.pr3}')


M = Mov_price('Lower class',20,'Dress circle',80,'Balcony',150)
M.price()