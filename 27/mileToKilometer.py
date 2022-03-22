from tkinter import *

window = Tk()

window.title("Miles to Kilometer (Milestone projects")
window.minsize(640,480)
window.config(padx=50,pady=80)

labelMiles = Label(text="Enter Miles here: ",font=("Verdana",14,"bold"))
labelMiles.grid(row=1, column=1)
labelKM = Label(text="Here's your KM: ",font=("Verdana",14,"bold"))
labelKM.grid(row=4, column=1)

input = Entry(font=("Verdana",14,"bold"))
input.grid(row=1, column=2)

labelNew = Label(text="")
labelNew.grid(row=4, column=2)

def convert():
    labelNew = Label(text=float(input.get())*1.609344 ,font=("Verdana",14,"bold"))
    labelNew.grid(row=4, column=2)

convertButton = Button(text="Convert to KM", command=convert)
convertButton.grid(row=1,column=3)







window.mainloop()