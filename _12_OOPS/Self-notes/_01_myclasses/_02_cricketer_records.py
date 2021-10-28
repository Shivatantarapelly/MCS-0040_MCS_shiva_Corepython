# printing the record of cricketer when the method is called

class Cricketer:
    def __init__(self, Dtest, Dodi, Dt20, stest, sodi, st20):
        self.dtest = Dtest
        self.dodi = Dodi
        self.dt20 = Dt20
        self.stest = stest
        self.sodi = sodi
        self.st20 = st20

    def dhoni(self):
        print('number of runs scored in Test:', self.dtest)
        print('number of runs scored in ODI:', self.dodi)
        print('number of runs scored in T20:', self.dt20)

    def sachin(self):
        print('number of runs scored in Test:', self.stest)
        print('number of runs scored in ODI:', self.sodi)
        print('number of runs scored in T20:', self.st20)


C = Cricketer(10000, 14000, 6000, 15000., 16000, 8000)
C.dhoni()

