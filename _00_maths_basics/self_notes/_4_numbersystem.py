for i in range(1,20):
    if i%2 == 0:
        print(i,' is even number')
    else:
        print(i, ' is odd number')

num = int(input('enter a num'))
bo = True
for i in range(2,num):
    if i% num == 0:
        print('number is not prime')
        bo = False
        break
if bo == True:
    print('number is prime')


