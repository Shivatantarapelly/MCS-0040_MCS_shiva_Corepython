# Append chars to string at end
'''
CRUD : update
state : string
behaviour : for, if, else, ==, +=

'''
# ---- algorithm ----

string = str(input('enter a string:'))
c = str(input('enter a character to append at end:'))

ns = string + c
print(ns)

string = str(input('enter a string:'))
c = str(input('enter a character to append at end:'))
ns = ''
for i in range(len(string) + 1):
    if i == len(string):
        ns += c
        break
    else:
        ns += string[i]

print(ns)

# ---- function ----

s = str(input('enter a string:'))
ch = str(input('enter a character to append at end:'))


def add_string(string, c):
    ns = string + c
    print(ns)


add_string(s, ch)
