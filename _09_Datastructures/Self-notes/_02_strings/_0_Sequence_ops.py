# String sequence operations

message = 'hello welcome to python'
print(message)

print("----String with for loop--------")
for char in message:
    print(char)

print("----String with for loop--------")
for char in message[0:10]:
    print(char)

print("----String with for loop--------")
for char in message[::-1]:
    print(char)

# SEQUENCE OPERATIONS
message = 'HELLO WORLD'
print("----------1. Indexing---------")
# 1. Indexing:
print("3rd index  : ", message[3])
print("6th index  : ", message[6])
# print("11th index : ", message[11])
# print("13th index : ", message[13])
print("-1 index   : ", message[-1])
print("-2 index   : ", message[-2])

print("----------2. Slicing---------")
# 2. Slicing :
message = 'hi good evening'
print("2 to 5 : ", message[2:5])
print("3 to 7 : ", message[3:7])
print("-9 to 5 : ", message[-9:5])

print("----------3. Adding---------")
# 3. Adding :
str1 = 'hi'
str2 = 'kumar'
print("Addition :", str1 + str2)
print("Addition :", str2 + str1)

str1 = 'Hello '
str2 = 'World'
print("Addition :", str1 + str2)
print("Addition :", str2 + str1)

print("----------3. Multiplying---------")
# 4. Multiplying
str1 = 'kumar '
print(str1[3])
print("Multiplication :", str1 * 10)

print("----------4. Membership ---------")
# 5. Checking for membership
print("H  : ", 'H' in 'HELLO-PYTHON')
print("L  : ", 'L' in 'HELLO-PYTHON')
print("LL  : ", 'LL' in 'HELLO-PYTHON')
print("PH  : ", 'PH' in 'HELLO-PYTHON')
print("-  : ", '-' in 'HELLO-PYTHON')
print("Space  : ", ' ' in 'HELLO PYTHON')
print("B  : ", 'B' not in 'HELLO PYTHON')
message = 'HELLO-PYTHON'
print('H' in message)
print('L' in message)

str1 = 'HelloWorld'  # Refer ASCII table  A-Z 65    a-z 97....

print("----------6. Length ---------")
# 6. len()
print("Length of string : ", len(str1))
# 7. max()
print("----------7. Max ---------")
print("Max of string : ", max(str1))

# 8. min()
print("----------8. Min ---------")
print("Min of string : ", min(str1))
