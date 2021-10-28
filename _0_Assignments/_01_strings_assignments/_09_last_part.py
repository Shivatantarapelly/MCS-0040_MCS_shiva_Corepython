
# Removing last party of the string by taking a character as the input from user

'''
CRUD : update
state : string
behaviour :
'''

# ----- builtin --------

string = 'Success is not final, failure is not fatal'
print(string)
char = str(input('enter a character from where you want to skip:'))
ns = string.rsplit(char,1)
print('the new string is :',ns[0])

# ---- algorithm ----





