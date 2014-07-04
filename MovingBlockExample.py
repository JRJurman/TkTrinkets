import tkinter as Tkinter
win = Tkinter.Tk()
can = Tkinter.Canvas(win, width=400, heigh=400)
can.pack()
for i in range(0, 420, 20):
	can.create_line(0, i, 400, i, fill="grey")
	can.create_line(i, 0, i, 400, fill="grey")

snake = {}
snake["pos"] = [10, 10]
snake["id"] = can.create_rectangle(100, 100, 100+20, 100+20, fill="blue")
snake["dir"] = [0, -1]

def updateDirection(event):
	if event.char=="w":
		snake["dir"] = [0, -1]
	if event.char=="s":
		snake["dir"] = [0, 1]
	if event.char=="a":
		snake["dir"] = [-1, 0]
	if event.char=="d":
		snake["dir"] = [1, 0]

can.bind("<Key>", updateDirection)
can.focus_force()

def updateSnake():
	op = snake["pos"]
	snake["pos"] = [snake["pos"][0] + snake["dir"][0],
					snake["pos"][1] + snake["dir"][1]]
	if snake["pos"][0] > 38 or snake["pos"][0] < 0:
		snake["pos"] = op
		return;
	if snake["pos"][1] > 38 or snake["pos"][1] < 0:
		snake["pos"] = op
		return;
	snake["pos"] = [snake["pos"][0] + snake["dir"][0],
					snake["pos"][1] + snake["dir"][1]]
	print(snake["pos"])
	can.move(snake["id"], snake["dir"][0]*20, snake["dir"][1]*20)

def timerFired():
	updateSnake()
	can.after(100, timerFired)

if __name__ == '__main__':
	timerFired()
	win.mainloop()
	
