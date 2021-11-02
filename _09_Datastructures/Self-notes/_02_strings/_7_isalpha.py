print("isalpha".center(40,'_'))
print("The isalpha() method returns True if all characters in the string are alphabets. If not, it returns False.")

name = "kumar"
print(name.isalpha()) # True

num = "123456"
print(num.isalpha()) # False

num1 = "kumar1234"
print(num1.isalpha()) #False



name = "kumar 12 3 4"
num = []
str = []
x=name.split()
print(x)
for i in x:
    print(i)
    if i.isdigit():
        num.append(i)
    elif i.isalpha():
        str.append(i)
print(num)
print(str)
