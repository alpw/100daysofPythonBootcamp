import pandas

data = pandas.read_csv("50_states.csv")
allStates = data["state"].to_list()
print(allStates)

status = True

while status:
    answer = input("State: ")
    if answer in allStates:
        allStates.remove(answer)
        theAns = data[data.state == answer]
        print(int(theAns["x"]), int(theAns["y"]))
    if answer == "w":
        status = False


listMiss = []
listX = []
listY = []

for state in allStates:
    o = data[data.state == state]
    listMiss.append(state)
    listX.append(int(o["x"]))
    listY.append(int(o["y"]))

missDict = {  "Missed States": listMiss,
        "X":listX,
        "Y":listY}

df = pandas.DataFrame(missDict)

df.to_csv("missed_states.csv")