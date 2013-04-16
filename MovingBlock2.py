import tkinter as Tkinter
win = Tkinter.Tk()

can = Tkinter.Canvas(win, width=200, height=200)
can.pack()

rec = {}
rec["id"] = can.create_rectangle(25, 25, 75, 75, fill="green")
rec["pos"] = 0

def moveRec():
    rec["pos"] = (rec["pos"] + 1) % 40
    if (rec["pos"] < 10):
        can.move(rec["id"], 10, 0)
    elif (rec["pos"] < 20):
        can.move(rec["id"], 0, 10)
    elif (rec["pos"] < 30):
        can.move(rec["id"], -10, 0)
    elif (rec["pos"] < 40):
        can.move(rec["id"], 0, -10)

def timerFired():
    moveRec(rec)
    can.after(50, timerFired)

if __name__ == '__main__':
	timerFired()
	win.mainloop()
	