for i in range(1,16):
    if i%3 == 0 and i%5 == 0:
        print('FizzBuzz')
    elif i%3 == 0 and i%5 != 0:
        print('Fizz')
    elif i%5 == 0 and i%3 != 0:
        print('Buzz')
    else:
        print(i)


for i in range(1,10):
    if i%3 == 0 or i%5 == 0:
        print(i)

