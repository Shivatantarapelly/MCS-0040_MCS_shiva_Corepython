'''
The else keyword catches anything which isn't caught by the preceding conditions.
'''
'''mail = 'shivatantarapelly@gmail.com'
if 'shiva' in mail:
    print(mail)
else:
    print('re- enter the mail')
mail = 'tantarapelly@gmail.com'
if 'shiva' in mail:
    print(mail)
else:
    print('re- enter the mail')
'''
'''light = int(input("enter 1 for 'on' or 0 for 'off:"))
if light == 1:
    print('lights on')
else:
    print('lights off')
if light == True:
    print('lights on')
else:
    print('lights off')
'''
'''age = 25
if age>=18:
    print('you are eligible to vote')
else:
    print('you are not eligible')
'''

'''num = int(input('enter a number'))
if num%2 == 0:
    print('num is even')
else:
    print('num is odd')
'''
'''
m1 = int(input('enter m1 marks'))
m2 = int(input('enter m2 marks'))
if m1 >= 35 and m2 >= 35:
    print('you are pass in maths subjects')
else:
    print('you are failed in maths')
'''
'''user = str(input('Do you want recipt yes or no:'))
if user != 'no':
    print('here is your receipt')
else:
    print('thank you')

user = int(input('Do you want recipt 1 or 0:'))
if user == 1:
    print('here is your receipt')
else:
    print('thank you')
'''
'''
pin = int(input('enter your mobile pin:'))
if pin == 1234:
    print('unlocked')
else:
    print('Try again')
'''
'''l = ['python','java']
print('available books:',l)
user = str(input('please select'))
if user != 'java':
    print('done python')
else:
    print('done java')
'''
'''
l = ['python','java','.net','csharp']
user = input('enter the course name')
if user in l:
    print('course is available')
else:
    print('course is not available')
'''
'''
u1 = input('enter 1st course:')
u2 = input('enter 2nd course')
if u1 in l and u2 in l:
    print('both courses are available')
else:
    print('oops sorry')
'''

'''True = 1  Cannnot be aasign values to true or false hence code will not executed    
False = 0
a = 1
b = 0
if False:
    print('okkk')
else:
    print('try again')
'''