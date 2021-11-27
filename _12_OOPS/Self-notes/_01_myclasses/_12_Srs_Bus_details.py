# displaying the bus details of srs going from bangalore to hyd

class Srs:
    def __init__(self, time, bp, dp, bn):
        self.time = time
        self.bp = bp
        self.dp = dp
        self.bn = bn

    def details(self):
        print('-----the details of your bus are------')
        print(f'time: {self.time}')
        print(f'Boarding point: {self.bp}')
        print(f'Dropping point: {self.dp}')
        print(f'Bus No: {self.bn}')


S = Srs('20:00', 'Mathahalli', 'MGBS', 'TS07ug75687')
S.details()
