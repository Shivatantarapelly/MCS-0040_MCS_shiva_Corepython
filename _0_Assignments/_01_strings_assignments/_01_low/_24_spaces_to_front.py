# move spaces to the front of a given string

'''

CRUD : update
state : string ,int
behaviour : for, if, ==, continue, +=

taking a string as user input and initialising a empty string and variable with zero
using for loop iterating the given string and using if condition storing the count of spaces in string
using for loop iterating the given string and using if condition removing the spaces from string
using the for loop printing the spaces according to count value and printing new string with out spaces

'''

string = str(input('enter a string:'))
ns = ' '
ct = 0
for i in string:
    if i == ' ':
        ct += 1
for j in string:
    if j == ' ':
        continue
    else:
        ns += j
for k in range(ct):
    print(' ', end='')

print(ns)

s = str(input('enter a string:'))
n = ' '
c = 0


# ------ function -------

def space_to_front(string, ns, ct):
    for i in string:
        if i == ' ':
            ct += 1
    for j in string:
        if j == ' ':
            continue
        else:
            ns += j
    for k in range(ct):
        print(' ', end='')

    print(ns)


space_to_front(s, n, c)
