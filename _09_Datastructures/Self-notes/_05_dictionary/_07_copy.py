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

print('----------------------------------------BUILT-IN-FUNCTIONS----------------------------')
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

print('---------------- -------3.retrieve items from employee data----------- ')
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

print('----------------------------5.clear()---------------------')

print("before clear                            :", emp_data)
print("after clear  employee data              :", emp_data.clear())

print('----------------------------6.copy    ---------------------')

dict1 = {'name': 'kumar', 'id': 30, 'location': 'banglure'}
print("dictionary                               :", dict1)
dict2 = dict1.copy()
print("dictionary2                              :", dict2)
dict1['name'] = 'kiran'
print("updated dictionary                       :", dict1)
print("dictionary2                              :", dict2)
