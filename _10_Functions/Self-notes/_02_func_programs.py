# taking start and end number as input and displaying the even and odd numbers
"""
# ------state---------
start = int(input('enter starting number: '))
end = int(input('enter ending number: '))
Even = []
Odd = []


# ------ Behaviour ------

def even_odd(s, e):
    for i in range(s, e + 1):
        if i % 2 == 0:
            Even.append(i)
        else:
            Odd.append(i)
    return Even, Odd


even_odd(start, end)
print('even numbers are: ', Even)
print('Odd numbers are: ', Odd)

# --------- state ---------
start = int(input('enter starting number: '))
end = int(input('enter ending number: '))
li = []


# ------- Behaviour ----------
def prime(s, e):
    num = 1
    for i in range(s, e + 1):
        if i > 1:
            for j in range(2, i):
                if i % j == 0:
                    num = 0
                    break
                else:
                    num = 1
            if num == 1:
                li.append(i)
        else:
            continue
    return li


print('prime number are: ', prime(start, end))

# taking my name as string and find the length of string without using built in function

name = 'shiva prasad'


def length(n):
    i = 0
    count = 0
    while i < len(n):
        count += 1
        i += 1
    return count


print('length of string :', length(name))

# passing a list to a function  and displaying the biggest number in the list

lis = [20, 45, 21, 80, 90, 42]


def big_num(l):
    val = l[0]
    for i in l:
        for j in range(0, (len(l))):
            if l[j] > i:
                if l[j] > val:
                    val = l[j]
                    break
    return val


print('biggest number is: ', big_num(lis))
"""
'''
# passing a list to a function  and displaying second largest number in the list

lis = [20, 45, 21, 80, 90, 42]


def sec_big_num(l):
    for i in range(len(l)):
        for j in range(len(l)):
            if l[i] < l[j]:
                l[i], l[j] = l[j], l[i]
    return l[-2]


print(sec_big_num(lis))
'''


def biggest(a, b, c):
    if a > b and a > c:
        return a
    elif b > c:
        return b
    else:
        return c


print('biggest number is :', biggest(10,20,30))
