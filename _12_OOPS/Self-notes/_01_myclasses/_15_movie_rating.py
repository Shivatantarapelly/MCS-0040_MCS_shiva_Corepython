# Displaying the rating of the movies

class Mov_rating:
    def __init__(self, m1, r1, m2, r2, m3, r3):
        self.m1 = m1
        self.r1 = r1
        self.m2 = m2
        self.r2 = r2
        self.m3 = m3
        self.r3 = r3

    def rating(self):
        print(f'Movie name: "{self.m1}"  Rating: {self.r1}')
        print(f'Movie name: "{self.m2}"  Rating: {self.r2}')
        print(f'Movie name: "{self.m3}"  Rating: {self.r3}')


m = Mov_rating('most eligible bachelor', 3.5, 'varun doctor', 4.0, 'varudu kavalenu', 4.1)
m.rating()