print("-----------------reverse()----------------------------")
print("The reverse() method reverses the elements of the list")

list = [1, 2, 3, 4, 5, 6, 7, 8]
print("normal list                  :", list)

list.reverse()
print("reversed list                :", list)


num = [10,11,13,14,15,16]
print("normal list                   :",num)
num.reverse()
print("reversed list                 :",num)



str= ['kumar','yuvi','kiran']
print("normal string is              :",str)
str.reverse()
print("after reverse string           :", str)


list1 =[1,'kumar',10.09]
print("collection of list             :",list1)
list1.reverse()
print("reversed list                  :",list1)


cities = ['hyd','bang','chennai','tirupathi','atp']
print("--------------cities in reversed---------------------")
for city in reversed(cities):
    print(city)

