print(
    "The Python popitem() method removes and returns the last element (key, value) pair inserted into the dictionary.")

stu_data = {
    'name': 'kumar',
    'roll_no': 27,
    'clg_name': 'jntuh',
    'location': 'hyd'
}
print("student details".ljust(40, '_'), ':', stu_data)
stu_data.popitem()
print("popped item".ljust(40, '_'), ":", stu_data)
stu_data.popitem()
print("popped item".ljust(40, '_'), ":", stu_data)
stu_data.popitem()
print("popped item".ljust(40, '_'), ":", stu_data)








