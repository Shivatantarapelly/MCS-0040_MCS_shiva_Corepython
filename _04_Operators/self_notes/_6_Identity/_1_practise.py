'''
6. identity operators( is):
'''
a = 10
b = 10
print('1:',a is b)  #true
print('2:',a is not b)  #false
a = 1,2,3
b = 1,2,3
print('3:',a is b)  #true sa the address are same
a = [1,2,3]
b = [1,2,3]
print('3:',a is b)  #false because both adress are not same
a = b  # assigning same address
print('4:',a is b)  #true as the address are same


