import tkinter as Tkinter
top = Tkinter.Tk()
can = Tkinter.Canvas(top, width=300, height=300)
can.pack()

for i in range(0, 320, 20):
    can.create_line(0, i, 300, i, fill="grey")
    can.create_line(i, 0, i, 300, fill="grey")
    
def drawSq(event):
    x = (event.x // 20)*20
    y = (event.y // 20)*20
    can.create_rectangle(x, y, x+20, y+20,
                         fill="yellow", outline="grey")
    
can.bind("<Button-1>", drawSq)

if __name__ == '__main__':
    top.mainloop()
