'''
there are two types of loop in python
1. for loop
2. while loop
while loop: With the while loop we can execute a set of statements as long as a condition is true.
'''

#displaying number upto 10

'''i = 1
while i<=10:
    print(i)
    i += 1
'''

#displaying number by taking user input limiting max input upto 100
'''
i = int(input('enter number upto where you want to display:'))
if i >= 0 and i <= 100:
    j = 1
    while j <= i:
        print(j,end=' ')
        j += 1
else:
    print('enter the number b/w 1 to 100 only')
'''

#taking the user input and printing even
'''
num = int(input('enter a number upto where you want even numbers:'))
if num > 0:
    i = 1
    print('--even numbers--')
    while i <= num:
        if i%2 == 0:
            print(i,end=' ')
        i += 1
else:
    print('enter valid number)
'''
#taking user input and printing odd number
'''
num = int(input('enter a number upto where you want odd numbers:'))
if num > 0:
    i = 1
    print('--Odd numbers--')
    while i <= num:
        if i%2 != 0:
            print(i,end=' ')
        i += 1
else:
    print('enter valid number)
'''

#taking two user input and printing the b/w numbers which are divisible 5
'''
user1 = int(input('enter start number:'))
user2 = int(input('enter ending number:'))
if user1 < user2 and user1 > 0 and user2 > 0:
    print('--the numbers divisible by 5 are--')
    while user1 <= user2:
        if user1%5 == 0:
            print(user1,end=' ')
        user1 += 1
else:
    print('enter valid start and ending pair')
'''
#taking two user inputs and printing number which are divisible by 3 and 10

'''
user1 = int(input('enter start number:'))
user2 = int(input('enter ending number:'))
if user1 < user2 and user1 > 0 and user2 > 0:
    print('--the numbers divisible by 5 are--')
    while user1 <= user2:
        if user1%3 == 0 and user1%10 == 0:
            print(user1,end=' ')
        user1 += 1
else:
    print('enter valid start and ending pair')
'''
'''
# taking one string input and taking another character input and printing the count of character that present in the
# string
user = str(input('enter a string:'))
user1 = str(input('enter a character to find how many times it repeates in string:'))
if len(user) > 2 and len(user1) == 1:
    i = 0
    count = 0
    while i <= len(user)-1:
        if user[i] == user1:
            count += 1
        i += 1
    print(f'count of {user1} in {user} is : {count}')
else:
    print('enter valid input')


#taking the user input and printing the characters of string line by line
u = str(input('enter string:'))
i = 0
while i < len(u)-1:
    print(u[i])
    i += 1
'''
'''
#printing numbers which are divisible by 8 or 9 upto 1000
x = 1
print('----the number divisible by 8 and 9 are---')
while x <= 1000:
    if x%8 == 0 or x%9 == 0:
        print(x,end=' ')
    x += 1


#taking a number as a user input and printing whether it is a prime number or not
'''
'''
x = int(input('enter a number: '))
if x>0:
    isprime = False
    i = 2
    while i < x:
        if x%i == 0:
            isprime = False
            break
        else:
            isprime = True
        i += 1
    if isprime:
        print(x,'is a prime number')
    else:
        print(x,'is not a prime number')
else:
    print('enter valid input')
'''
'''
#taking a number as a input and returning list of all prime numbers upt that number
x = int(input('enter a number: '))
if x>0:
    i = 1
    l = []
    while i <= x:
        if i > 1:
            isprime = True
        else:
            isprime = False
        j =2
        while j < i:
            if i%j == 0:
                isprime = False
                break
            j += 1
        if isprime:
            l.append(i)
        else:
            pass
        i += 1
    print('----prime number----')
    print(l)
else:
    print('enter valid input')
'''
'''
#printing the odd number upto user enter number

user = int(input('enter a number:'))
if user > 0:
    i = 1
    print('---odd number---')
    while i<=user:
        if i%2 == 1:
            print(i,end=' ')
        i += 1
else:
    print('enter valid input')
'''

#displaying number in pattern shape
'''
1
1 2
1 2 3

user = int(input('Enter number of rows : '))

i = 1
while i <= user:
    j = 1
    while j <= i:
        print(j, end=" ")
        j += 1
    print()
    i += 1
'''
# getting o/p as below by taking no of rows as input
'''
4 3 2 1
3 2 1
2 1
1 
'''
'''
user = int(input('Enter number of rows : '))
i = 1
while i <= user:
    j = user
    while j >= i:
        print(j,end=' ')
        j -= 1
    print()
    i += 1
'''


