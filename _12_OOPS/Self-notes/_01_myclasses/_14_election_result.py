
# displaying the election result when the method is called

class Election_res:
    def __init__(self,t,c,b):
        self.t = t
        self.c = c
        self.b = b

    def amberpet(self):
        print(f'{self.t} has won the election here')

    def lbnagar(self):
        print(f'{self.c} has won the election here')

    def karimnagar(self):
        print(f'{self.b} has won the election here')


E = Election_res('TRS','CONGRESS','BJP')
E.amberpet()
