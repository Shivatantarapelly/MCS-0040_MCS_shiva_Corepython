# Replace first occurance character

'''
CRUD : update
state : string
behaviour : for

'''

# ---- built in  ----

s = 'hi shiva'
s1 = s.replace('h', 'H', 1)
print(s1)

# --- algorithm ---

s = 'good morning'
s1 = ' '
for i in range(len(s)):
    s1 = s.replace(s[i], 'G', 1)
    break
print(s1)

# ---- function ----

S = str(input('enter a string:'))
S1 = ' '


def fst_occur(s, s1):
    for i in range(len(s)):
        u = s[i].upper()
        s1 = s.replace(s[i],u, 1)
        break
    print(s1)


fst_occur(S, S1)
