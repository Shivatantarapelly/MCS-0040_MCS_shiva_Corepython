
# write a program and fetch the data using http get and point out number of holidays in england
# and wales then group them based on year


from urllib.request import urlopen
import json

url = 'https://www.gov.uk/bank-holidays.json'
data = urlopen(url)

data_json = json.loads(data.read())
print(type(data_json))
"""
for key,value in data_json.items():
    if key == "england-and-wales":
        ndata1 = value
        for k,v in ndata1.items():
            if k == 'events':
                ndata2 = v

dic2 = {}
count = 0
for i in ndata2:
    dic1 = i
    print(dic1['title'],'---- ',dic1['date'])
    count += 1
    for ke,va in dic1.items():
        if ke == 'title' or ke == 'value':
"""
count = 0
lis1 = []
dic = {}
for i in data_json['england-and-wales']['events']:
    lis1.append(i['title'])
    lis1.append(i['date'])
    # print(i['title'],'--------->',i['date'])
    count += 1
cnt = 0
year = 2016
st = 0
for i in range(len(lis1)):
    if year == 2016 or year == 2022:
        if lis1[i] != "Christmas Day":
            pass
        else:
            dic[year] = lis1[st:i+2]
            year += 1
            st = i+2
    else:
        if lis1[i] != "Boxing Day":
            pass
        else:
            dic[year] = lis1[st:i+2]
            year += 1
            st = i+2

print(dic)
print('Total number of holidays',count)
for key,value in dic.items():
    print(f'the holiday in {key} is : {len(value)//2}')


# print(lis1)
# lis2 = []
# for i in range(2016,2023):
#     lis2.append(i)
# print(lis2)
# lis1 = str(lis1)
# for i in lis2:
#     print(f'the holiday year {i} is {lis1.count(str(i))}')
#

