from tkinter import *

top=Tk()

resStr=StringVar()
resStr.set("Enter Numbers and Click add")

num1Label=Label(text="First Number")
num1Label.pack()
num1Entry=Entry()
num1Entry.pack()

num2Label=Label(text="Second Number")
num2Label.pack()
num2Entry=Entry()
num2Entry.pack()

resultLabel=Label(textvariable=resStr)
resultLabel.pack()

def addNo():
    no1=int(num1Entry.get())
    no2=int(num2Entry.get())
    no3=no1+no2
    resStr.set("The sum is "+str(no3))

but=Button(text="Add",command=addNo)
but.pack()
top.mainloop()
