'''
writing n number of if condition inside another if are said to be nested if
'''

'''year = int(input('enter year:'))
if year%4 == 0:
    if year%100 == 0:
        if year%400 == 0:
            print(year.'is a leap year')
        else:
            print(year,'is not a leap year')
    else:
        print(year,'is a leap year')
else:
    print(year,'is not a leap year')


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





