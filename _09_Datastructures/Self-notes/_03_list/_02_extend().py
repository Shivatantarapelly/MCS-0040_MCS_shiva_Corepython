print("-------------------extend----------------------------")
print("The extend() method adds all the elements of an iterable(like strings,list.tuple,dict) to the end of the list.")
list = [1, 2, 3, 4]
print("before list           :", list)
list.extend([10, 11, 13])
print("after extend list     :", list)
list.append([18, 19, 20])
print("after append list     :", list)
list.extend(['kumar', 'yuvi'])
print("after extend the list :", list)

print("-----------both append and extend---------------")

data = []
data.append(1)
data.append(2)
data.append(3)
data.append(4)
data.append(5)
print("after append the data is            :", data)
data.append([10, 19, 20])
print("after append the data is            :", data)
data.extend([10])
print("after extend the data is            :", data)
data.extend([19, 100, 143])
print("after extend the data is            :", data)


data1 = [1,2,3]
print("normal data                         :", data1)
data1.extend([10,19,20,'kumar',10.09])
print("after extend the data  is           :", data1)