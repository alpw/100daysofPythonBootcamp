import pandas

data = pandas.read_csv("2018_Central_Park.csv")
furs = data["Primary Fur Color"].tolist()

mydict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count":[ furs.count("Gray"), furs.count("Cinnamon"), furs.count("Black")]
    }

dFrame = pandas.DataFrame(mydict)
dFrame.to_csv("Colors")