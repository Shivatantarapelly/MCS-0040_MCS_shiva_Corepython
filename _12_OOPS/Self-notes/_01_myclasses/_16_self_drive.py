# displaying self drive car details when ever the method is called

class Self_drive:
    def __init__(self, o, r, z, op, rp, zp):
        self.o = o
        self.r = r
        self.z = z
        self.op = op
        self.rp = rp
        self.zp = zp

    def details(self):
        print(f'"{self.o}" self drive cars. The price per day is: Rs {self.op}')
        print(f'"{self.r}" self drive cars. The price per day is: Rs {self.rp}')
        print(f'"{self.z}" self drive cars. The price per day is: Rs {self.zp}')


s = Self_drive('Ola', 'Revv', 'Zoom', 2000, 2500, 3000)
s.details()
