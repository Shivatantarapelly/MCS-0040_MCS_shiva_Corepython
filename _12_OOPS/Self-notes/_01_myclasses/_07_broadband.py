
# displaying the broadband prices when the fuction is called

class Broadband:
    def __init__(self, act, pr1, nl, pr2, hw, pr3):
        self.act = act
        self.pr1 = pr1
        self.nl = nl
        self.pr2 = pr2
        self.hw = hw
        self.pr3 = pr3

    def price(self):
        print(f'the name of OTT is: "{self.act}" and price is: {self.pr1}')
        print(f'the name of OTT is: "{self.nl}" and price is: {self.pr2}')
        print(f'the name of OTT is: "{self.hw}" and price is: {self.pr3}')


B = Broadband('Act fibre',3500,'Neolog',2400,'Hathway',3000)
B.price()