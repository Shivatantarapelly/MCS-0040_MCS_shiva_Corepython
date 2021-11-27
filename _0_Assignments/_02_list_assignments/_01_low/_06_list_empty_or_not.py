# Check list is empty or not

"""
CRUD : Retrieve
state: List
Behaviour: if, not, ==
"""

# ---- Algorithms ------


myList = []

if len(myList) == 0:
    print("The list is empty.")
else:
    print("The list is not empty.")

myList = []

if not myList:
    print("The list is empty.")
else:
    print("The list is not empty.")

myList = []

if not bool(myList):   # if bool(mylist) == False

    print("The list is empty.")
else:
    print("The list is not empty.")
