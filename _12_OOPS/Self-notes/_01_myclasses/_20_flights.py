# displaying the flight details from bangalore to hyd


class Flight:
    def __init__(self, f1, b1, d1, f2, b2, d2, f3, b3, d3):
        self.f1 = f1
        self.b1 = b1
        self.d1 = d1
        self.f2 = f2
        self.b2 = b2
        self.d2 = d2
        self.f3 = f3
        self.b3 = b3
        self.d3 = d3

    def details(self):
        print('----The details of trains available from bangalore to hyd----')
        print(f'Flight name: {self.f1}  Boarding time : {self.b1} Dropping time: {self.d1}')
        print(f'Flight name: {self.f2}  Boarding time : {self.b2} Dropping time: {self.d2}')
        print(f'Flight name: {self.f3}  Boarding time : {self.b3} Dropping time: {self.d3}')


F = Flight('Air Asia', '18:00', '20:00', 'Indigo', '21:00', '23:30', 'spice jet', '02:00', '04:00')
F.details()
