
# Displaying the OTT prices when the user call the price method


class Ott_price:
    def __init__(self,pv,pr1,ah,pr2,nf,pr3):
        self.pv = pv
        self.pr1 = pr1
        self.ah = ah
        self.pr2 = pr2
        self.nf = nf
        self.pr3 = pr3

    def price(self):
        print(f'the name of OTT is: "{self.pv}" and price is: {self.pr1}')
        print(f'the name of OTT is: "{self.ah}" and price is: {self.pr2}')
        print(f'the name of OTT is: "{self.nf}" and price is: {self.pr3}')


o = Ott_price('prime video',999,'aha',399,'netflix',1200)
o.price()