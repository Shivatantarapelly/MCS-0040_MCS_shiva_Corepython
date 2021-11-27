
# displaying the price of mobile rechrge of diffenent networks

class Mob_network:
    def __init__(self, at, pr1, ji, pr2, bl, pr3):
        self.at = at
        self.pr1 = pr1
        self.ji = ji
        self.pr2 = pr2
        self.bl = bl
        self.pr3 = pr3

    def price(self):
        print(f'the name of network is: "{self.at}" and price is: {self.pr1}')
        print(f'the name of network is: "{self.ji}" and price is: {self.pr2}')
        print(f'the name of network is: "{self.bl}" and price is: {self.pr3}')


M = Mob_network('Airtel',400,'Jio',350,'Bsnl',450)
M.price()