import pandas
from pandas.core.algorithms import mode

data = pandas.read_csv("weather_data.csv")
print(type(data["temp"]))


#myDict = data.to_dict()
#print(myDict)

myList = data["temp"].to_list()
#print(myList)

print(sum(myList)/len(myList))

print(data["temp"].mean())  #like mean value theorem
print(data["temp"].max())

print(data["condition"])
print("#"*30)
print(data.condition)

monday = data[data.day == "Monday"]     #wow
#print(monday)
print(monday.condition)

#printing the highest temp
print(data[data.temp == data["temp"].max()])

#celcius to fahrenheit

print(monday.temp*9/5 + 32) #or
tempInt = int(monday.temp)
print(tempInt*9/5 +32)

#to dictionary
data_dict = {
"students": ["alpern","demir","ve","diğerleri"],
"scores": [99,98,12,22]
}
myFrame = pandas.DataFrame(data_dict)

myFrame.to_csv("new.csv")