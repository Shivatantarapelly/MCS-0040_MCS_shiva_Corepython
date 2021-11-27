'''
writing n number of if condition inside another if are said to be nested if
'''
# taking year as user input and giving o/p as leap year or not a leap year
'''
year = int(input('enter year:'))
if year > 0 and year <= 2021:
    if year%4 == 0:
        if year%100 == 0:
            if year%400 == 0:
                print(year,'is a leap year')
            else:
                print(year,'is not a leap year')
        else:
            print(year,'is a leap year')
    else:
        print(year,'is not a leap year')
else:
    print('enter valid year')
'''

'''
#validating the hall ticket number present in data base and display pass or fail and future planning
dic = {123:'pass',456:'fail',789:'pass',101112:'fail'}
num = int(input('enter you examination number:'))
if num in dic:
    print('you have',dic[num])
    if dic[num] == 'pass':
        print('please enter 1 to continue or 2 to discontinue the education')
        num = int(input('enter your choice 1 or 2:'))
        if num == 1:
            print('-----you have decided to continue-----')
            print('enter 1 for inter and 2 for diploma')
            num = int(input('enter your choice 1 0r 2:'))
            if num == 1:
                print('-----you have decided to do inter----')
                print('enter 1 for M.P.C and 2 for B.I.P.C')
                n1 = int(input('enter your choice 1 or 2'))
                if n1 == 1:
                    print('----you have decided to do M.P.C---')
                else:
                    print('----you have decided to do B.I.P.C')
                    print('enter 1 for govt collage and 2 for private collage')
                    n1 = int(input('enter your choice 1 0r 2'))
                    if n1 == 1:
                        print('----you have choosen govt collage----')

                    else:
                        print('you have choosen private collage')
            else:
                print('----you have decided to do diploma----')
        else:
            print('----you have decided to dicontinue the studies----')
    else:
        print('enter 1 for reapplying and 2 for stop')
        n1 = int(input('enter your choice 1 or 2:'))
        if n1 == 1:
            print('----you have successfully reapplied for exam----')
        else:
            print('----you have stopped your studies----')
else:
    print('enter valid examination number')

print('-----thank you-----')
'''
#taking the user inputs and displaying accordingly the brands and and finally their respective prices
'''
mobiles = {'samsung': 10000,'oppo':15000,'vivo':20000,'iphone':50000}
tv = {'samsung': 40000,'lg': 50000,'mi': 20000,'sony': 45000}
laptops = {'lenovo': 40000,'hp': 50000,'acer':30000}
print('enter 1:mobiles 2:Tv 3:Laptops')
u1 = int(input('enter your choice:'))
if u1 == 1:
    print('available mobiles:',mobiles.keys())
    u1 = input('enter your mobile choice:')
    if u1 == 'samsung':
        print('price of samsung mobile is',mobiles['samsung'])
    elif u1 == 'oppo':
        print('price of oppo mobile is', mobiles['oppo'])
    elif u1 == 'vivo':
        print('price of vivo mobile is', mobiles['vivo'])
    elif u1 == 'iphone':
        print('price of oppo mobile is', mobiles['iphone'])
    else:
        print('mobile is not available')
elif u1 == 2:
    print('available mobiles:',tv.keys())
    u1 = input('enter your TV choice:')
    if u1 == 'samsung':
        print('price of samsung TV is',tv['samsung'])
    elif u1 == 'lg':
        print('price of lg tv is', tv['lg'])
    elif u1 == 'mi':
        print('price of mi tv is', tv['mi'])
    elif u1 == 'sony':
        print('price of sony tv is', tv['sony'])
    else:
        print('Tv is not available')
elif u1 == 3:
    print('available laptops:',laptops.keys())
    u1 = input('enter your laptop choice:')
    if u1 == 'lenovo':
        print('price of lenovo laptop is',laptops['lenovo'])
    elif u1 == 'hp':
        print('price of hp laptop is', laptops['hp'])
    elif u1 == 'acer':
        print('price of acer laptop is', laptops['acer'])
    else:
        print('mobile is not available')
else:
    print('enter valid option')
'''

# taking the user input and validating whether it matches with data base, displaying accordingly and finally showing
#price of respective cars
'''
print('enter the car of your choice to know the price from below')
print('1:maruti 2:toyota 3:mahindra')
user = int(input('enter your choice:'))
if user == 1:
    print('1:swift 2:baleno 3:dezire')
    user = int(input('enter your choice:'))
    if user == 1:
        print('---you have selceted swift---')
        print('1: automatic 2: manual')
        user = int(input('enter your choice:'))
        if user == 1:
            print('the price of swift automatic is Rs:1000000/-')
        elif user == 2:
            print('print price of swift manual is Rs:8000000')
        else:
            print('enter valid option')
    elif user == 2:
        print('---you have selceted Baleno---')
        print('1: automatic 2: manual')
        user = int(input('enter your choice:'))
        if user == 1:
            print('the price of Baleno automatic is Rs:1400000/-')
        elif user == 2:
            print('print price of Baleno manual is Rs:1200000')
        else:
            print('enter valid option')
    elif user == 3:
        print('---you have selceted Dezire---')
        print('1: automatic 2: manual')
        user = int(input('enter your choice:'))
        if user == 1:
            print('the price of Dezire automatic is Rs:1200000/-')
        elif user == 2:
            print('print price of Dezire manual is Rs:1000000')
        else:
            print('enter valid option')
    else:
        print('enter valid option')
elif user == 2:
    print('1:fortuner 2:etios')
    user = int(input('enter your choice:'))
    if user == 1:
        print('---you have selceted Fortuner---')
        print('1: automatic 2: manual')
        user = int(input('enter your choice:'))
        if user == 1:
            print('the price of fortuner automatic is Rs:3000000/-')
        elif user == 2:
            print('print price of fortuner manual is Rs:1000000')
        else:
            print('enter valid option')
    elif user == 2:
        print('---you have selceted Etios---')
        print('1: automatic 2: manual')
        user = int(input('enter your choice:'))
        if user == 1:
            print('the price of Etios automatic is Rs:1300000/-')
        elif user == 2:
            print('print price of Etios manual is Rs:11000000')
        else:
            print('enter valid option')
elif user == 3:
    print('1:xuv500 2:tuv300')
    user = int(input('enter your choice:'))
    if user == 1:
        print('---you have selceted XUV 500---')
        print('1: automatic 2: manual')
        user = int(input('enter your choice:'))
        if user == 1:
            print('the price of XUV500 automatic is Rs:2500000/-')
        elif user == 2:
            print('print price of XUV500 manual is Rs:2000000')
        else:
            print('enter valid option')
    elif user == 2:
        print('---you have selceted TUV300---')
        print('1: automatic 2: manual')
        user = int(input('enter your choice:'))
        if user == 1:
            print('the price of TUV300 automatic is Rs:1800000/-')
        elif user == 2:
            print('print price of TUV300 manual is Rs:1500000')
        else:
            print('enter valid option')
else:
    print('enter valid option')
'''

#taking tha age as the user input and displaying whether he is eligible for applying for the driving license or not
'''
age = int(input('enter your age:'))
if age>0 and age<100:
    if age>=18:
        print('----you are eligible to apply for driving licence----')
        print('----do you have adhaar card----')
        print('press 1: for yes and 0 : for no')
        a = int(input('please enter:'))
        print('---do you have pan card---')
        print('press 1: for yes and 0 : for no')
        p = int(input('please enter:'))
        if a == 1 and p == 1:
            print('you would be charging Rs:1000/- for applying')
            print('press 1: for yes and 0 : for no')
            print('---Please Confirm---')
            c = int(input('please enter here:'))
            if c == 1:
                print('you have successfully applied')
                print('------happy driving-----')
            else:
                print('transaction failed')
        else:
            print('sorry we need both adhar and pan for applying')
    else:
        print('you are not eligible for applying for driving licence')
else:
    print('enter valid age')
'''





