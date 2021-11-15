import csv

data = open('E:\MCS-0040_MCS_shiva_Corepython\_15_File_Handling\Self-notes\phone_dataset.csv', 'r')
read = csv.reader(data)
list1 = []
list2 = []
for i in read:
    # for j in range(len(i)):
    #     # i = i[j].strip(" ' ")
    # x = i.split(',')
    list1.extend(i)
print(list1)
data1 = open('E:\MCS-0040_MCS_shiva_Corepython\_15_File_Handling\Self-notes\query - Copy.txt', 'r')
for data in data1.readlines():
    data = data.strip('\n')
    list2.append(data)
list1.sort()
print(list1)
print(list2)

for i in list2:
    for j in range(len(list1)):
        if i in list1[j]:
            print(f'matches {i} : details {list1[j]}')
