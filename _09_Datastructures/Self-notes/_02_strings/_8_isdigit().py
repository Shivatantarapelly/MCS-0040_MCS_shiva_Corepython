print("isdigit".center(40, '_'))
print(
    "The isdigit() method returns True if all characters in a string are digits. If not, it returns False.")

num = "12345"
print("the number  ",num.isdigit())  # True

str = "1234kumar"
print("string ",num.isdigit())   # True

str1 = "kumar12345kumar"
print("string1",str1.isdigit())        #False
