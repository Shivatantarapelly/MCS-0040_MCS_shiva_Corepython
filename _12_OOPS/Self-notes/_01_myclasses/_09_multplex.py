# displaying the screens and movies the are being played when the method is called


class Multiplex:
    # state
    def __init__(self, s1, m1, s2, m2, s3, m3):
        self.s1 = s1
        self.m1 = m1
        self.s2 = s2
        self.m2 = m2
        self.s3 = s3
        self.m3 = m3

    # Behaviour
    def details(self):
        print(f'the movie name :"{self.m1}" screen: {self.s1}')
        print(f'the movie name :"{self.m2}" screen: {self.s2}')
        print(f'the movie name :"{self.m3}" screen: {self.s3}')


M = Multiplex(1, 'RRR', 2, 'Radheshyam', 3, 'KGF2')
M.details()
