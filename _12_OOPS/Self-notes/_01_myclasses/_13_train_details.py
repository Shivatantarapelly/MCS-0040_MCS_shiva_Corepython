# displaying the train details which are there to hyd from bang

class Train:
    def __init__(self, t1, b1, d1, t2, b2, d2, t3, b3, d3):
        self.t1 = t1
        self.b1 = b1
        self.d1 = d1
        self.t2 = t2
        self.b2 = b2
        self.d2 = d2
        self.t3 = t3
        self.b3 = b3
        self.d3 = d3

    def details(self):
        print('----The details of trains available from bangalore to hyd----')
        print(f'Train name: {self.t1}  Boarding place and time : {self.b1} Dropping place and time: {self.d1}')
        print(f'Train name: {self.t2}  Boarding place and time : {self.b2} Dropping place and time: {self.d2}')
        print(f'Train name: {self.t3}  Boarding place and time : {self.b3} Dropping place and time: {self.d3}')


T = Train('Garibrath', 'ksr bengaluru(18:00)', 'kachiguda(05:00)', 'duranto', 'yeswanthapur(19:00)',
          'secundrabad(06:00)', 'Rajdhani', 'yelhanka(14:00', 'secundrabad(07:00)')
T.details()
