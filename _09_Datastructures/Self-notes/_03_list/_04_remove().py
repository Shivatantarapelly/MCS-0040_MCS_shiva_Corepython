print("--------------------------remove()-----------------------")
print("remove()...its remove the  particular item ,"
      "in that list duplicates items is there,its remove first matching item ")

names = ['karthik', 'hari', 'yuvi', 'raj', 10, 20, 30]
names.remove('yuvi')                           #  give only one argument
print("after removing, names is         :", names)


"""names.remove()
print(names)    # TypeError: list.remove() takes exactly one argument (0 given)
"""


names.remove('kumar')    # ValueError: list.remove(x): x not in list