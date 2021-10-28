# displaying the highest no. of wins of teams in ipl

class Ipl_wins:
    def __init__(self, mi, csk, kkr, srh):
        self.mi = mi
        self.csk = csk
        self.kkr = kkr
        self.srh = srh

    def win(self):
        print('The no. of wins by MI: ', self.mi)
        print('The no. of wins by CSK: ', self.csk)
        print('The no. of wins by KKR: ', self.kkr)
        print('The no. of wins by SRH: ', self.srh)


I = Ipl_wins(5, 4, 2, 2)
I.win()
