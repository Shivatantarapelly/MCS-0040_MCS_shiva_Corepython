# getting the voter details by calling a method in class

class Voter:
    def __init__(self, area, vid, age):
        self.area = area
        self.vid = vid
        self.age = age

    def shiva(self):
        print('voter id:', self.vid)
        print('area :', self.area)
        print('age :', self.age)


v = Voter('Amberpet', 1234, 25)
v.shiva()
