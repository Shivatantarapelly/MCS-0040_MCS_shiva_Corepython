print('----------------------pop()-----------------------------')
print('The pop() method removes the item at the given index from the list ')
data  = [1,2,3,4,5,6,7,8]
print("normal data            :", data)
data.pop()
print("after pop the data     :", data)

# particular index value will be deleted

data.pop(1)
print("after pop the data     :", data)
data.pop(2)
print("after pop the data     :", data)

x=data.pop(3)
print("pop item is            :",x)
print("after pop the data     :",data)

print("-----------------negative index also pop-------------------")

x=data.pop(-1)
print("popped item is          :",x)

print("after the pop ,data is :",data)




