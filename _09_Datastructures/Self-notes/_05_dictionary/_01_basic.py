"""
Dictionary :
    - Mutable data structure
    - Unordered
    - Key value pair i.e, item
    Key properties:
        - Keys must be UNIQUE
        - Keys must be IMMUTABLE and values can be anything
"""

stu_det = {'name': 'kumar', 'roll_num': 20, 'adder': 'atp'}
print("student details             :", stu_det)

# keys is unique

stu_det = {'name': 'raju', 'loc': 'hyd', 'name': 'kumar'}
print("student details is          :", stu_det)

# keys must be immutable (keys>>>> number,float,string,boolean,tuple)

dict1 = {
    100: 'number',
    26000.5: 'salay',
    'name': 'kumar',
    True: 'permanent',
    (1, 2, 4, 5): (1, 2, 2, 3,),
}
print("dictionaty1                 :", dict1)

# in keys place not using list,set dict

print('---------------------------employee data--------------------')
emp_data = {
    'id': 27,
    'name': 'kumar',
    'salary': 27000.00,
    'loc': 'banglure',
    'company': 'MCS'
}

print("employee data             :", emp_data)
print("-----------------------print key and value--------------------")
for key,value in emp_data.items():
    print(key,'----',value)

print('-----------------------print only keys-------------------------')

for key in emp_data.keys():
    print(key)

print('-----------------------print only values-----------------------')

for value in emp_data.values():
    print(value)




