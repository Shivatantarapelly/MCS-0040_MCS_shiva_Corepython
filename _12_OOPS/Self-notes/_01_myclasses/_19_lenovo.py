# displaying the lenovo laptop prices as per there processors

class Lenovo:
    def __init__(self, i3, i5, i7, i9, p3, p5, p7, p9):
        self.i3 = i3
        self.i5 = i5
        self.i7 = i7
        self.i9 = i9
        self.p3 = p3
        self.p5 = p5
        self.p7 = p7
        self.p9 = p9

    def prices(self):
        print(f'the price of {self.i3} processor is Rs: {self.p3}')
        print(f'the price of {self.i5} processor is Rs: {self.p5}')
        print(f'the price of {self.i7} processor is Rs: {self.p7}')
        print(f'the price of {self.i9} processor is Rs: {self.p9}')


L = Lenovo('i3', 'i5', 'i7', 'i9', 35000, 40000, 45000, 50000)
L.prices()
