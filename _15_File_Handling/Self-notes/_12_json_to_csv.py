from urllib.request import urlopen
import json
import csv

url = urlopen("https://www.gov.uk/bank-holidays.json")
data = json.load(url)
jsonfile = json.dumps(data)
key = ["england-and-wales","scotland","northern-ireland"]
key2 = ["division","events"]
csvfile = open("csvfile1.csv",'w')
csvfile.write(jsonfile)
csvfile.close()

with open('csvfile1.csv','r') as csvfile:
    data = csvfile.read()
    print(data)

