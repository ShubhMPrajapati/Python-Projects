from tkinter import Tk, Button, Label, Text, Entry


window = Tk()
window.title('Miles to Km Converter')
window.config(padx=20, pady=20)


label1 =  Label(text="")
label1.grid(column=0, row=0)


input = Entry(width=7)
input.grid(column=1, row=0)


label2 = Label(text="Miles")
label2.grid(column=2, row=0)



label3 = Label(text="is Equal to")
label3.grid(column=0, row=1)


label5 = Label(text="")
label5.grid(column=1, row=1)



label4 = Label(text="KM")
label4.grid(column=2, row=2)


def calculate():
    text = int(input.get())
    text *= 1.609
    new_text = int(text)
    label5.config(text=new_text)

button = Button(text="Calculate", command= calculate)
button.grid(column=1, row=2)


window.mainloop()
