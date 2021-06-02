from tkinter import *

top=Tk()

Label(top,text="First Name").grid(row="0")
Label(top,text="Last Name").grid(row="1")
e1=Entry(top)
e2=Entry(top)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)

top.mainloop()
