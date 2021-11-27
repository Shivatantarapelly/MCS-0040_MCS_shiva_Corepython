# remove spaces from a given string

'''
CRUD : update
state : string
behaviour : for , if, ==, +=

taking the user input as string and initializing an empty string
iterating the string using the for loop and using the condition removing the empty spaces
and printing the new string

'''

string = str(input('enter a string:'))
ns = ' '
for i in string:
    if i == ' ':
        continue
    else:
        ns += i

print('the new string with out spaces:',ns)

s = str(input('enter a string:'))


def remo_space(string):
    ns = ' '
    for i in string:
        if i == ' ':
            continue
        else:
            ns += i

    return ns


print('the new string with out spaces is:', remo_space(s))
