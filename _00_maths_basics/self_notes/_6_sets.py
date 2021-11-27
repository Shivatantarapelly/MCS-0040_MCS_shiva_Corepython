a = {1,2,3,4,5}
b = {1,2,5,6,8}
print(a-b)  #gives output as element of a which are not present in b
print(b-a)  #gives output as element of b which are not present in a
print("union",a.union(b))
print("intersection ",a.intersection(b))
