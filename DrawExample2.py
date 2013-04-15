import tkinter as Tkinter
top = Tkinter.Tk()
can = Tkinter.Canvas(top, width=300, height=300)
can.pack()
can.focus_set()

colors = {
	"r":"red",
	"b":"blue",
	"g":"green",
	"y":"yellow"
}

brush = {"color":"blue"}

for i in range(0, 310, 10):
    can.create_line(0, i, 300, i, fill="grey")
    can.create_line(i, 0, i, 300, fill="grey")

def drawSq(event):
	x = (event.x // 10)*10
	y = (event.y // 10)*10
	can.create_rectangle(x, y, x+10, y+10, fill=brush["color"], outline="grey")

def drawWhite(event):
	x = (event.x // 10)*10
	y = (event.y // 10)*10
	can.create_rectangle(x, y, x+10, y+10, fill="grey95", outline="grey" )

def setColor(event):
	print(repr(event.char))
	if event.char in colors:
		brush["color"] = colors[event.char]

can.bind("<Button-1>", drawSq)
can.bind("<Key>", setColor)
can.bind("<Double-Button-1>", drawWhite)

if __name__ == '__main__':
    top.mainloop()