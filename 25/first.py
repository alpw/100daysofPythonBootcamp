# with open("weather_data.csv") as file:
#     data = file.readlines()
#     print(data)

import csv

#with open("weather_data.csv") as file:
#    data = csv.reader(file)
#    temps = []
#    for row in data:
#        if row[1] != "temp":
#            temps.append(row[1])
#    print(temps)

import pandas

data = pandas.read_csv("weather_data.csv")
print(data["temp"])