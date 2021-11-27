class Travels:
    start_pt = 'Hyderabad'
    end_pt = 'Bangalore'

    def __init__(self, t1, t2, t3, t4):
        self.t1 = t1
        self.t2 = t2
        self.t3 = t3
        self.t4 = t4

    def t1_details(self, st, et):
        print(f'Travels Name: {self.t1}')
        print(f'Boarding Time: {st} dropping Time: {et}')

    def t2_details(self, st, et):
        print(f'Travels Name: {self.t2}')
        print(f'Boarding Time: {st} dropping Time: {et}')

    def t3_details(self, st, et):
        print(f'Travels Name: {self.t3}')
        print(f'Boarding Time: {st} dropping Time: {et}')

    def t4_details(self, st, et):
        print(f'Travels Name: {self.t4}')
        print(f'Boarding Time: {st} dropping Time: {et}')

    @classmethod
    def st_end(cls):  # only allowing class variables
        print(f'From: {Travels.start_pt} To: {Travels.end_pt}')

    @staticmethod
    def sta():  # only allowing class variables to access
        print(f'{Travels.start_pt} {Travels.end_pt}')


T = Travels('SRS', 'ORANGE', 'MORNINGSTAR', 'VRL')
Travels.st_end()
T.t1_details('21:00', '22:00')
Travels.sta()
print(T.t1)  # accessing instance variables
