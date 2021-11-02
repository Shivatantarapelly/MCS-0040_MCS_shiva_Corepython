print("-----------------1.append------------")
print("append().... It appends element(any value) at end of the list")

list1 = [1, 2, 3, 4, 5]
print("before append          :", list1)
list1.append(10)
print("after append           :", list1)

list1.append(15)
print("after append           :", list1)

list1.append(20)
print("after append           :", list1)

list1.append('kumar')
list1.append([1, 2, 3, 4])
list1.append((5, 6, 7, 8))
list1.append({9, 8, 7})
print("updated list is         :", list1)
list1.append({'one': 1})
print("updated list is         :", list1)

for index, value in enumerate(list1):
    print(index, "-----", value)
