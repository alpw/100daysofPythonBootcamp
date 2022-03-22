#file = open("weather_data.csv")
#data = file.readlines()
#
#for i in data:
#    print(i)
#
#file.close()

#import csv
#
#file = open("weather_data.csv")
#data = csv.reader(file)
#
#newList = []
#for row in data:
#    print(row)
#    newList.append(row[1])
#
#file.close()
#
#print(newList[1::])

import pandas

data = pandas.read_csv("weather_data.csv")
dataDict = data.to_dict()

print(data)
print(data["temp"])
print(type(data["temp"]))
print(dataDict)
print(type(dataDict))

dataList = data["temp"].to_list()
print(sum(dataList)/len(dataList))

print(data["temp"].mean())

print(data["temp"].max())

print(data.condition)   #same
print(data["condition"])#same

#get data in row
print(data[data.day == "Monday"])
print("#"*50)
print(data[data.temp == max(data["temp"].to_list())])
monday = data[data.day == "Monday"]
print(int(monday.temp)*9/5 +32)

#Creating a dataframe

myDict = {
    "pc":["asus","monster","toshiba"],
    "benchmark":[3,9,7]
}
newFrame = pandas.DataFrame(myDict)
print(newFrame)
newFrame.to_csv("newDataFrame")