print("set".center(40, '_'))
set = {}
print("set".ljust(40, '_'), ":", set)
print("type".ljust(40, '_'), ":", type(set))

print("sequence items".center(40, "_"))
print("numbers".center(40, '_'))
set = {1, 2, 3, 4, 5, 6}
print("set", set)
print("type", type(set))

# set does not allow duplicate items
set = {1, 2, 3, 4, 6, 1, 2, 3}
print("set :", set)
set = {'hi', 'hello', 'kiran', 'yuvi'}
print("strings in set", set)

set1 = {'one': 1, 'two': 2}
print("set", set1)

print("collection of datatypes".center(40, "_"))

set2 = {1, 2, 3, (10, 11, 12)}
print("set2".ljust(40, '_'), ":", set2)


