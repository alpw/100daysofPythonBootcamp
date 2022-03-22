import tkinter

window = tkinter.Tk()

window.title("new at dorm")
window.minsize(640,480)
window.config(padx=20,pady=20) #display components starting at(20,20)

label = tkinter.Label(text="Label bu", font=("Arial",24,"bold"))
label.grid(column=1,row=1)

label["text"] = "walla label"
label.config(text="vallah billah labeldir bu")

#typing smt
input = tkinter.Entry()
input.grid(column=3, row=1)

def kliklendin():
    print("aloooğ")
    label["text"] = input.get()

#creating button
buton = tkinter.Button(text="bas banağğ", command=kliklendin)
buton.grid(column=2, row=2)


input2 = tkinter.Entry()
input2.grid(column=4, row=3)



# pack(mid left right), place(x,y), grid(column=0, row=0)_using like excel



window.mainloop()
