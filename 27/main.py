import tkinter

window = tkinter.Tk()


window.title("Proğğgram")
window.minsize(640,480)

suchALabel = tkinter.Label(text="Label olacak bu", font=("Arial",24,"bold"))   #nothing

suchALabel.pack(side="left")   #now we can see


#label: text
suchALabel.config(text="dulduldul", )
suchALabel["text"] = "ula label değişti noli la"


def clicked():
    print("you fuckn clicked")
    newText = entry.get()
    suchALabel.config(text=newText)


#button
button = tkinter.Button(text="pls fuckn click me", command=clicked)
button.pack()

#entry smt
entry = tkinter.Entry(width=11)
entry.pack()







window.mainloop()