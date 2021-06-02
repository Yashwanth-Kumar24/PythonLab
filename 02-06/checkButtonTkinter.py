from tkinter import *

top=Tk()
'''
resStr=StringVar()
resStr.set("Click to view selected")
Label(top,textvariable=resStr).grid(row="0")
'''

var1=IntVar()
Checkbutton(top,text="Coding",variable="var1").grid(row=1,sticky=W)
var2=IntVar()
Checkbutton(top,text="Sports",variable="var2").grid(row=2,sticky=W)
var3=IntVar()
Checkbutton(top,text="Music",variable="var3").grid(row=3,sticky=W)


'''
def res():
    a=var1.get()
    b=var2.get()
    c=var3.get()
    l=[a,b,c]
    print(p.state())
    s=""
    s+="You chose the following\n"
    print(a,b,c)
    if(l[0]==1):
        s+="Coding\n"
    if(l[1]==1):
        s+="Sports\n"
    if(l[2]==1):
        s+="Music\n"
    resStr.set(s)
Button(top,text="View",command=res).grid(row="4")'''
top.mainloop()

