import tkinter as Tkinter
win = Tkinter.Tk()
label = Tkinter.Label(win, text ="Hello World")
label.grid(row=0, column=0)

def chgColor(color):
    label.config(fg=color)

def chgSize(size):
    label.config(font=("arial", size))

scl = Tkinter.Scale(win, from_=10, to_=16, orient="horizontal")
scl.grid(row=1, column=0)
scl.config(command=chgSize)

but0 = Tkinter.Button(win, text="Blue")
but0.grid(row=1, column=1)
but0.config(command=lambda:chgColor("Blue"))

but1 = Tkinter.Button(win, text="Red")
but1.grid(row=2, column=1)
but1.config(command=lambda:chgColor("Red"))

but2 = Tkinter.Button(win, text="Green")
but2.grid(row=3, column=1)
but2.config(command=lambda:chgColor("Green"))

if __name__ == '__main__':
	win.mainloop()