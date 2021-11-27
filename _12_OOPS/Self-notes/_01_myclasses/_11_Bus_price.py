
# displaying the bus prices of different travels from ban  - hyd

class Bus_price:
    # state
    def __init__(self, srs, m1, org, m2, mrs, m3):
        self.srs = srs
        self.m1 = m1
        self.org = org
        self.m2 = m2
        self.mrs = mrs
        self.m3 = m3

    # Behaviour
    def details(self):
        print('-----The details of buses and prices from hyd to Bangalore-----')
        print(f'the Travels name :"{self.srs}" Price:Rs {self.m1}')
        print(f'the Travels name :"{self.org}" Price:Rs {self.m2}')
        print(f'the movie name :"{self.mrs}" Price:Rs {self.m3}')


B = Bus_price('SRS',1000,'Orange',1200,'Morningstar',1400)
B.details()
