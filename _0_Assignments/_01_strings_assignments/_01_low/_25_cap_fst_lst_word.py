# capitalize first and last letters of each word of a given string
'''

CRUD : update
state : string, list
behaviour : for, = , +


taking the user input as string and initialising an empty list
split the string to list and iterating the list and changing the first and last letters of word to upper
and appending into a new list
'''

string = str(input('enter a string:'))
nl = []

s = string.split()
for i in s:
    i = i[:0] + i[0].upper() + i[1:]
    i = i[:-1] + i[-1].upper()
    nl.append(i)
for j in nl:
    print(j, end=' ')

# ----- function -------
print()

s = str(input('enter a string:'))
n = []


def cap_fst_lst_word(string, nl):
    ns = string.split()
    for i in ns:
        i = i[:0] + i[0].upper() + i[1:]
        i = i[:-1] + i[-1].upper()
        nl.append(i)
    for j in nl:
        print(j, end=' ')


cap_fst_lst_word(s, n)
