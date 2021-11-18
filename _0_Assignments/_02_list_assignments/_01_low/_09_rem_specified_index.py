# Remove specified index from list and print

# ---- builtin -----

ls = [10, 20, 30, 40, 50]
x = int(input('enter the index number of element you want to remove:'))
del ls[x]
print(ls)


ls = [1, 2, 3, 4, 5]
x = int(input('enter the index number of element you want to remove:'))
ls.pop(x)
print(ls)

# ---- algorithm -----

lis = [1, 2, 3, 4, 5]
idx = int(input('enter the index number of element you want to remove:'))
