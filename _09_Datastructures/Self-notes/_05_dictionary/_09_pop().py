print("pop".center(50,'_'))
print("The pop() method removes and returns an element from a dictionary having the given key.")


stu_data = {
    'name' : 'kumar',
    'roll_no':27,
    'clg_name':'jntuh',
    'location':'hyd'
}
print("student details".ljust(40,'_'),':',stu_data)
print("popped  item  ".ljust(40,'_'),':',stu_data.pop('name'))
print("updated student details".ljust(40,'_'),":",stu_data)
