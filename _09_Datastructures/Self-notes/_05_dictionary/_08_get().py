emp_data = {
    'id': 27,
    'name': 'kumar',
    'salary': 27000.00,
    'loc': 'banglure',
    'company': 'MCS',
}

print("employee data                 :",emp_data)
print("employee id                   :",emp_data['id'])
print("employee name                 :",emp_data['name'])
# print("employee firstname            :",emp_data['firstname']) # KeyError: 'firstname' # avoid exception we use get()
print("employee  id                  :",emp_data.get('id'))
print("employee  name                :",emp_data.get('name'))
print("employee firstname            :",emp_data.get('firstname'))
print("employee firstname            :",emp_data.get('firstname','kumar'))
print("employee firstname            :",emp_data.get('firstname'))