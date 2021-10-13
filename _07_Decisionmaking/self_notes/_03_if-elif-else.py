'''age = int(input('enter your age:'))
if age > 18:
    print('you are eligible to vote')
elif age == 17:
    print('Please wait one year')
else:
    print('you are not eligible to vote')
'''
'''
a,b,c = 10,20,30
if a>b and a>c:
    print('a is the higest number')
elif b>c:
    print('b is the highest number')
else:
    print('c is the highest number')
'''
'''
d = {123:'shiva',456:'prasad',789:'sai'}
user = int(input('enter your password:'))
if user not in d:
    print('enter valid password')
elif user == 123:
    print('hi shiva')
elif user == 456:
    print('hi prasad')
else:
    print('hi sai')
'''
'''
l = ['sai@gmail','shiva@gmail','prasad@gmail']
u1 = input('enter your mail id:')
u2 = int(input('enter password:'))
if u1 in l and u2 in d:
    print('welcome',d[u2])
elif u1 in l and u2 not in d:
    print('you have entered wong password')
elif u1 not in l and u2 in d:
    print('you have entered wrong username')
else:
    print('both username and password is wrong')
'''
'''
d = {100:{'name':'shiva','age':26,'course':'python'},
     200:{'name':'sai','age':25,'course':'java'},
     300:{'name':'hari','age':27,'course':'.net'}}
u1 = int(input('enter employee id: ')
if u1 == 100:
    print(d[100])
elif u1 == 200:
    print(d[200])
elif u1 == 300:
    print(d[300])
else:
    print('enter valid details')
'''
'''
u1 = 0
user1 = int(input('enter the floor you want to go i.e 0,1,2,3: '))
if user1 == 1:
    print('wecome to 1st floor')
elif user1 == 2:
    print('welcome 2nd floor')
else:
    print('welcome to 3rd floor')
'''
'''
marks = int(input('enter marks:'))
if marks >= 80:
    print('you have passed with A+ grade')
elif marks >= 60:
    print('you have passed with A grade')
elif marks >= 50:
    print('you have passed with B grade')
elif marks >= 35:
    print('you have passed with C grade')
else:
    print('you have failed')
'''
'''
a,b,c = 10,20,30
if a>b and a>c:
    print(a,'is the highest number')
elif b>c:
    print(b,'is the highest number')
else:
    print(c,'is the highest number')
'''
'''
year = int(input('enter year to find its a leap year or not:'))
if year % 4 == 0 and year % 100 !=0:
    print(year,'is a leap year')
elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
    print(year,'is a leap year')
else:
    print('it is not a leap year')
'''
'''
y = int(input('enter year:'))
if y%4 == 0 and y%100 != 0 or y%400 == 0:
    print(y,'is a leap year')
else:
    print(y,'is not a leap year')
'''