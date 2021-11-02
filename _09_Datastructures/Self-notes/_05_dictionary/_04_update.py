emp_data = {
    'id': 27,
    'name': 'kumar',
    'salary': 27000.00,
    'loc': 'banglure',
    'company': 'MCS',
}

print("employee data                         :", emp_data)

# length()
print("--------------length of the dictionary---------------")
print("length of the dictionary               :", len(emp_data))

# type()
print("type of the employee data              :", type(emp_data))

# id()
print("address of employee data               :", id(emp_data))

print(
    '----------------------------------------BUILT-IN-FUNCTIONS----------------------------')
emp_data = {
    'id': 27,
    'name': 'kumar',
    'salary': 27000.00,
    'loc': 'banglure',
    'company': 'MCS',
}

print("employee data                         :", emp_data)

print("-----------1.retrieve keys from dictionary---------------------")
print('keys from employee data        :', emp_data.keys())
print('------ retrieve keys using for loop -------')
for keys in emp_data.keys():
    print(keys)

for ind, key in enumerate(emp_data, start=0):
    print(ind, '----', key)

print("--------------------2.retrieve values from employees--------------- ")

print("retrieve values from employee data   :", emp_data.values())
print('------------retrieve values using for loop--------')
for value in emp_data.values():
    print(value)

print(
    '---------------- -------3.retrieve items from employee data----------- ')
for key, value in emp_data.items():
    print(key, '-----', value)
print('--------------------------4.  update dictionary---------------------')
print("---------------------------update employee data-----------------------------------")

print('before updating  employee data          :', emp_data)
emp_data['name'] = 'kiran'
print("after updated name ,employee data       :", emp_data)

emp_data['loc'] = 'hyd'
print("after updated location ,employee data   :", emp_data)

emp_data['company'] = 'TCS'
print("after updated company ,employee data    :", emp_data)

dict1 = {'name': 'kumar', 'id': 27, 'company': 'MCS'}
dict2 = {'number': 9877777}
dict1.update(dict2)
print("updated dict1                           :", dict1)
dict2.update(dict1)
print("updated dict2                           :", dict2)

stu_data = {
    'name': 'kumar',
    'roll_no': 27,
    'clg_name': 'jntuh',
    'location': 'hyd'
}
print("student details".ljust(40, '_'), ':', stu_data)

stu_data.update({"mob_num": 9876555})
print("student details".ljust(40, '_'), ':', stu_data)
