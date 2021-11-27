# Substring replacement

"""
CRUD : update
state : string, list, int, none
behaviour: for , !=, ==
"""

string = str(input('enter a string:'))
substring1 = str(input('enter the substring you want to replace:'))
substring2 = str(input('enter a new substring you want to replace:'))

ns = string.replace(substring1, substring2)
print(ns)


string = str(input('enter a string:'))
substring1 = str(input('enter the substring you want to replace:'))
substring2 = str(input('enter a new substring you want to replace:'))
st = 0
list1 = []
list2 = []

for i in range(len(string)):
    if string[i] != ' ' and string[i] != ',':
        if i == len(string) - 1:
            list1.append(string[st:i + 1])
        pass
    else:
        list1.append(string[st:i])
        st = i + 1
for i in list1:
    if i == '' or i == ',':
        pass
    else:
        list2.append(i)
for i in range(len(list2)):
    if list2[i] == substring1:
        list2[i] = substring2
print('--new string after replacing: ----')
for i in list2:
    print(i, end=' ')

# ----- function ------


s = str(input('enter a string:'))
sub1 = str(input('enter the substring you want to replace:'))
sub2 = str(input('enter a new substring you want to replace:'))
l1 = []
l2 = []


def substring_replace(string1, subs1, subs2, ls1, ls2):
    st1 = 0
    for idx in range(len(string1)):
        if string1[idx] != ' ' and string1[idx] != ',':
            if idx == len(string1) - 1:
                ls1.append(string1[st1:idx + 1])
            pass
        else:
            ls1.append(string1[st1:idx])
            st1 = idx + 1
    for idx in ls1:
        if idx == '' or idx == ',':
            pass
        else:
            ls2.append(idx)
    for idx in range(len(ls2)):
        if ls2[idx] == subs1:
            ls2[idx] = subs2
    print('--new string after replacing: ----')
    for idx in ls2:
        print(idx, end=' ')


substring_replace(s, sub1, sub2, l1, l2)
