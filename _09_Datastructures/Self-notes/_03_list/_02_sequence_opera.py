data = [1, 2, 10, 13, 16, 17, 19, 20, 22]  # create
print("normal data is                :", data)  # retrieve
data[0] = 123
print("updated data is               :", data)  # Update

del data[1]
print("after deleting updated data is:", data)  # delete

print('-----------------sequence operations---------------------')
print("----------1.indexing----------------")
#       0  1  2    3   4  5   6   7    8
data = [1, 2, 10, 13, 16, 17, 19, 20, 22]
#      -9 -8  -7  -6  -5  -4  -3   -2  -1

print("in data 0(zero)th index is               :", data[0])
print("in data  5th index is                    :", data[5])
print("in data -2 index is                      :", data[-2])
print("in data -1 index is                      :", data[-1])
print("in data -5 index is                      :", data[-5])
print("in data -3 index is                      :", data[-3])
print("in data  8 index is                      :", data[8])
print("in data  3 index is                      :", data[3])

print("-----------------------2.slicing operations------------------------")

#       0  1  2    3   4  5   6   7    8
data = [1, 2, 10, 13, 16, 17, 19, 20, 22]
#      -9 -8  -7  -6  -5  -4  -3   -2  -1


print("slicing operations 2 to end      :", data[2:])
print("slicing operations 2 to 5        :", data[2:5])
print("slicing operations  [:]          :", data[:])
print("slicing operations  [::]         :", data[::])
print("slicing operations  [:-2]        :", data[:-2])
print("slicing operations  [::3]        :", data[::3])
print("slicing operations  [3:-1]       :", data[3:-1])
print("slicing operations  [-3:-1]      :", data[-3:-1])
print("slicing operations  [-3:-1]      :",
      data[-3:-6])  # in slicing both negative indexes 2nd index is high
print("slicing operations  [7:-3]       :", data[7:-7])  # []

print("-------------------3.adding------------------------------------------")
list1 = [1, 2, 3, 4]
list2 = [2, 3, 4, 6]
print("adding of both lists               :", list1 + list2)

list3 = list1 + list2
print("adding  both lists                 :", list3)

print(
    "--------------------------------4. Multiplying-------------------------")
print("Multiply 2 lists :", [1, 2, 3] * 5)

print("multiplying                        :", [10, 12, 19, 20] * 3)

print(
    "--------------------------------5. Membership--------------------------")
print("Check value : ", 100 in data)
print("check value :", 50 in data)
print("check value :", 50 not in data)
print("Check value : ", 20 in data)
print("check value :", 40 in data)
print("check value :", 100 not in data)

print(
    "---------------------------------6. length-----------------------------")
print("Length of data         : ", len(data))

print(
    "---------------------------------7. max--------------------------------")
print("maximum value in data  : ", max(data))

print(
    "--------------------------------8. min---------------------------------")
print("minimum value in  data : ", min(data))




list = [1, 2, "kumar", 3, "kiran", 5, 6]
output# ["kumar,"kian, 1, 2]

"""for ind, i in enumerate(list, start=0):
    print(ind, i)
print(list[2], list[4], list[0], list[1])"""

"""list = [1, 2, "kumar", 3, "kiran", 5, 6]
a_string = str(list)

numbers = []
for list in a_string():
   if list.isdigit():
      numbers.append(int(list))0
print(numbers) """

a_string = "0abc 1 def 23"
numbers = []
for word in a_string.split():
   if word.isdigit():
      numbers.append(int(word))

print(numbers)

print(numbers)


