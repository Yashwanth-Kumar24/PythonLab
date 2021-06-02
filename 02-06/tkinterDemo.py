from tkinter import *

top=Tk()
hello=Label(text="Hi Friends")
hello.pack()
quitBut=Button(text="Quit",command=top.quit)
quitBut.pack()
top.mainloop()
