
data = {'A': [{'id': 10, 'name': 'shiva', 'salary': {'basic': 200, 'hr': 1200, 'sa': 4000}},
              {'id': 20, 'name': 'sai', 'salary': {'basic': 25000, 'hr': 1000, 'sa': 3000}},
              {'id': 30, 'name': 'prasad', 'salary': {'basic': 22000, 'hr': 1300, 'sa': 5000}}],
        'B': [{'fname': 'shiva', 'lname': 't', 'location': 'hyderabad'},
              {'fname': 'sai', 'lname': 'j', 'location': 'banglore'},
              {'fname': 'prasad', 'lname': 'p', 'location': 'chennai'}]}
lst = []
for clname, key in data.items():
    if clname == 'A':
        adata1 = key
    else:
        bdata = key


class A:

    def __init__(self, lstitem):
        self.lstitem = lstitem

    def even_num_emp(self):
        if lsttem % 2 != 0:
            print('employee names at even numbers: ',self.lstitem['name'])

    def all_emp_details(self):
        for k, y in self.lstitem.items():
            if k == 'id' or k == 'name':
                print('all employee details',k, ':', y)

    def emp_salary(self, lst):
        for k, y in self.lstitem.items():
            if k == 'salary':
                for k1, y1 in y.items():
                    lst.append(y1)
                    print('actual pay: ',k1, ':', y1)
                    if lsttem == len(adata1) - 1:
                        if k1 == 'sa':
                            print('total sum of all salaries:',sum(lst))

    # a.emp_salary(lst)


class B(A):
    def __init__(self, lstitem, bdata):
        super().__init__(lstitem)
        self.bdata = bdata

    def having(self):
        res = 0
        for i in self.lstitem:
            for k, j in i.items():
                if k == 'name':
                    name = j
                elif k == 'salary':
                    for l, m in j.items():
                        res += m
                        if res > 10000:
                            print(name)
                            break
                else:
                    pass

    def emp_details(self):
        for i in bdata:
            for k, j in i.items():
                print(k, ':', j)

    def salary(self):
        for i in self.lstitem:
            res = 0
            for k, j in i.items():
                if k == 'name':
                    name = j
                elif k == 'salary':
                    for l, m in j.items():
                        res += m
                        if l == 'sa':
                            print(name, ':', res)

    def location_id(self):
        for i in range(len(self.lstitem)):
            for k,j in self.lstitem[i].items():
                for m,n in bdata[i].items():
                    if k == 'id' and m == 'location':
                        print(j, ':', n)


for lsttem in range(len(adata1)):
    a = A(adata1[lsttem])
    a.even_num_emp()
    # a.all_emp_details()
    # a.emp_salary(lst)

b = B(adata1, bdata)
print('employee name having salary above 10000')
b.having()
print('--------fnama and lastname and employee details--------')
b.emp_details()
print('---------salary of employees -------')
b.salary()
print('--------location according to id-----')
b.location_id()
