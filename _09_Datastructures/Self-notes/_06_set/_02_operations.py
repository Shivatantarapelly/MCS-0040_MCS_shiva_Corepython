set1 = {}
print("empty set".ljust(40, '_'), ":", set1)
print("type".ljust(40, '_'), ':', type(set1))  # dictionary

set1 = set()
print("empty set".ljust(40, '_'), ':', set1)
print("type".ljust(40, '_'), ':', type(set1))

set1 = set({})
print("empty set".ljust(40, '_'), ':', set1)
print("type".ljust(40, '_'), ':', type(set1))

set2 = {1, 2, 3, 4, 6, 10}
print("set2".ljust(40, '_'), ":", set2)

# duplicates not allowed
set3 = {1, 2, 3, 4, 10, 12, 1, 2}
print("set3".ljust(40, '_'), ":", set3)

print("update".center(40, '_'))
set3 = {1, 2, 3, 4, 10, 12, 1, 2}
print("set3".ljust(40, '_'), ":", set3)
set3.add(20)
print("updated set".ljust(40, '_'), ":", set3)
set3.add(30)
print("updated set".ljust(40, '_'), ":", set3)
set3.add('kumar')
print("updated set".ljust(40, '_'), ":", set3)
set3.add(19.08)
print("updated set".ljust(40, '_'), ":", set3)
"""set3.add(20,30)
print("updated set".ljust(40,'_'),":",set3)   # TypeError: set.add() takes exactly one argument (2 given)"""

print("discard".center(40, ("_")))
# removing element  # set.discard() takes exactly one argument (0 given)
print("before discard".ljust(40, '_'), ":", set3)
set3.discard('kumar')
print("after discard".ljust(40, '_'), ":", set3)

set3.discard(10)
print("after discard".ljust(40, '_'), ":", set3)

set3.discard(30)
print("after discard".ljust(40, '_'), ":", set3)
set3.discard(12)
print("after discard".ljust(40, '_'), ":", set3)
set3.discard(4)
print("after discard ".ljust(40, '_'), ":", set3)

set1 = {1, 2, 3, 4, 5}
print("set1".ljust(40, '_'), ":", set1)  # {1, 2, 3, 4, 5}

set2 = {3, 2, 5, 7, 9}
print("set2".ljust(40, '_'), ":", set2)  # {2, 3, 5, 7, 9}

print("set1 union set2".ljust(40, '_'), ":",
      set1.union(set2))  # {1,2,3,4, 5, 7, 9}
print("set1 difference set2".ljust(40, '_'), ":",
      set1.difference(set2))  # {1, 4}
print("set2 difference set1".ljust(40, '_'), ":",
      set2.difference(set1))  # {9, 7}
print("set1 interaction set2".ljust(40, '_'), ":",
      set1.intersection(set2))  # {2, 3, 5}
print("set1 symmetric_difference set2".ljust(40, '_'), ":",
      set1.symmetric_difference(set2))  # {1, 2, 3, 4, 5, 7, 9}
print("set1 issubset set2".ljust(40, '_'), ":", set1.issubset(set2))  # False
