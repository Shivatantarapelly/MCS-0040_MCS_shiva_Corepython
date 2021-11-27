print("--------------------conversions--------------------")
print("conversions---one data type to another data type")


num = 10
print("number is              :", num)
print("type of number         :", type(num))
print("address of the number  :", id(num))

print("---------convert integer to float----------")
print("number is              :", float(num))
print("type of number         :", type(num))
print("address of the number  :", id(num))

# assign a variable

x=float(num)
print("number is              :", x)
print("type of number         :", type(x))
print("address of the number  :", id(x))

print("-------------------float to integer--------------------")

salary = 25000.00
print("-------before converting---------")
print("salary is               :",salary)
print("type of salary is       :",type(salary))
print("address of the salary   :",id(salary))

print("--------after converting-----------")
sal = int(salary)
print("salary is               :",sal)
print("type of salary is       :",type(sal))
print("address of the salary   :",id(sal))

print("---------------------converting string to list-------------")
str= "kumar"
print("--------before converting ----------")
print("normal string is         :",str)
print("type of string           :",type(str))

print("-----after converting------")
str1= list("kumar")
print("normal string is         :",str1)
print("type of string           :",type(str1))


print("-------------------converting  list to string---------------")
print("-----before converting---------")
data = [1,2,3,4,5,6]
print("list is                  :",data)
print("type of list             :",type(data))

"""print("-------after converting---------")
list1 = str(data)
print("list is                  :",list1)
print("type of list             :",type(list1))
"""




