class A:
    var1 = "I'm in class A"
    def __init__(self):
        self.var1 ="I'm in class A constructor"

class B(A):
    var1 = "I'm in class B"
    def __init__(self):
        self.var1 = "I'm in Class B constructor"



c = B()

print(B.var1)