print("index".center(40,'_'))
print("The index() method returns the index of a substring inside the string (if found). "
      "If the substring is not found, it raises an exception.")

msg = "hello welcome to python programming language"
print("msg".ljust(40,'_'),':',msg)
print("index of 'to'".ljust(40,'_'),msg.index('to'))
print("index of 'o'".ljust(40,'_'),msg.index('o'))
print("index of 'he'".ljust(40,'_'),msg.index('he'))
print("index of 'll'".ljust(40,'_'),msg.index('ll'))
print("index of 'come'".ljust(40,'_'),msg.index('come'))
print("index of 'py'".ljust(40,'_'),msg.index('py'))
print("index of 'pro'".ljust(40,'_'),msg.index('pro'))
print("index of 'lan'".ljust(40,'_'),msg.index('lan'))
print("index of 'age'".ljust(40,'_'),msg.index('age'))
#print("index of 'mtt'".ljust(40,'_'),msg.index('mtt'))   # ValueError: substring not found

