# displaying the details of all ktm bikes when the method is called

class Ktm:
    def __init__(self, m1, m2, m3, c1, c2, c3, p1, p2, p3):
        self.m1 = m1
        self.c1 = c1
        self.p1 = p1
        self.m2 = m2
        self.c2 = c2
        self.p2 = p2
        self.m3 = m3
        self.c3 = c3
        self.p3 = p3

    def details(self):
        print(f'Model 1: {self.m1}  CC : {self.c1}  price: {self.p1}')
        print(f'Model 2: {self.m2}  CC : {self.c2}  price: {self.p2}')
        print(f'Model 3: {self.m3}  CC : {self.c3}  price: {self.p3}')


K = Ktm('Duke','RC','Adventure',200,250,390,180000,20000,250000)
K.details()
