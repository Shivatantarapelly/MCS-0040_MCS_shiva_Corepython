print('-----------------dictionary is  mutable------------------')

# CREATE
emp_data = {
    'id': 27,
    'name': 'kumar',
    'salary': 27000.00,
    'loc': 'banglure',
    'company': 'MCS'
}

# RETRIEVE
print("---------------------------retrieve employee data-----------------------------------")

print("employee data               :", emp_data)
print("employee salary             :", emp_data['salary'])
print('employee company            :', emp_data['company'])
print('employee location           :', emp_data['loc'])
print('employee  id                :', emp_data['id'])
print('employee name               :', emp_data['name'])

# UPDATE
print("---------------------------update employee data-----------------------------------")

print('before updating  employee data          :', emp_data)
emp_data['name'] = 'kiran'
print("after updated name ,employee data       :", emp_data)

emp_data['loc'] = 'hyd'
print("after updated location ,employee data   :", emp_data)

emp_data['company'] = 'TCS'
print("after updated company ,employee data    :", emp_data)

# DELETE
print('----------------------------------delete----------------------')

print("before deleting the employee data     :", emp_data)
del emp_data['id']
print("after deleted ,employee data          :", emp_data)

emp_data.clear()  # all data is deleted,structure is not deleted
print("after clear the employee data         :", emp_data)

del emp_data  # data and structure  deleted
