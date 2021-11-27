# Swapping chars in string

'''
CRUD : Update
state : string
Behaviour : for, if, elif, else, ==

'''

# ---- Algorithm ----

string = str(input('enter a string:'))
ns = ' '
print('enter index number of elements want to swap')
print('index number between 0 and', len(string) - 1)
num1 = int(input('enter 1st index number:'))
num2 = int(input('enter 2nd index number:'))
for i in range(len(string)):
    if i == num1:
        ns = string[:i] + string[num2] + string[i + 1:]
    elif i == num2:
        ns = ns[:i] + string[num1] + ns[i + 1:]
    else:
        pass
print(ns)

# ---- Function ------

s = str(input('enter a string:'))
n = ' '
print('enter index number of elements want to swap')
print('index number between 0 and', len(s) - 1)
Num1 = int(input('enter 1st index number:'))
Num2 = int(input('enter 2nd index number:'))


def swap(string, ns, num1, num2):
    for i in range(len(string)):
        if i == num1:
            ns = string[:i] + string[num2] + string[i + 1:]
        elif i == num2:
            ns = ns[:i] + string[num1] + ns[i + 1:]
        else:
            pass
    print(ns)


swap(s, n, Num1, Num2)

# ---- class -----


s = str(input('enter a string:'))
n = ' '
print('enter index number of elements want to swap')
print('index number between 0 and', len(s) - 1)
Num1 = int(input('enter 1st index number:'))
Num2 = int(input('enter 2nd index number:'))


class Swap:
    def __init__(self, string, ns, num1, num2):
        self.string = string
        self.ns = ns
        self.num1 = num1
        self.num2 = num2

    def swap(self):
        for i in range(len(self.string)):
            if i == self.num1:
                self.ns = self.string[:i] + self.string[self.num2] + self.string[i + 1:]
            elif i == self.num2:
                self.ns = self.ns[:i] + self.string[self.num1] + self.ns[i + 1:]
            else:
                pass
        print(self.ns)


s = Swap(s, n, Num1, Num2)
s.swap()
