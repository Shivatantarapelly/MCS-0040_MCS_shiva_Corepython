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

print('---------------------------BUILT-IN-FUNCTIONS-----------------------------')
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





stu_data = {
    'name' : 'kumar',
    'roll_no':27,
    'clg_name':'jntuh',
    'location':'hyd'
}
print("student details",stu_data)
print("keys in student data :",stu_data.keys())

for key in stu_data.keys():
    print(key)

