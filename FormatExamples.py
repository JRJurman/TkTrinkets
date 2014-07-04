#Pack Example
import Tkinter
win = Tkinter.Tk()
t1 = Tkinter.Label(win, text="Label One")
t2 = Tkinter.Label(win, text="Label Two")
t1.pack(side="top")
t2.pack(side="bottom")
t1.pack(side="left")
t2.pack(side="right")
t1.pack(side="top")
t2.pack(side="top")
t1.pack(side="bottom")
t2.pack(side="top")

#Place Example
win = Tkinter.Tk()
b1 = Tkinter.Button(win, text="Hello Button")
b1.place(relheight=1, relwidth=1)
b1.place(relheight=0.5, relwidth=0.5)
b1.place(relx=0.2, rely=0.2, relheight=0.5, relwidth=0.5)

#Grid Example
win = Tkinter.Tk()
cen = Tkinter.Label(win, text="Center")
cen.grid(row=1, column=1)
mov = Tkinter.Label(win, text="Moving")
mov.grid(row=0, column=0)
mov.grid(row=2, column=2)
mov.grid(row=0, column=1) #above
mov.grid(row=2, column=1) #below
mov.grid(row=1, column=1) #on top
mov.grid(row=0, column=0)