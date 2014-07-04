# create initial window
import tkinter as Tkinter
top = Tkinter.Tk()
top.title("Bingo Builder")

# create entry frame, for hitting buttons
entryFrame = Tkinter.Frame(top)
entryFrame.pack(side="left")

# a simple list widget, makes the window a bit bigger too!
entryList = Tkinter.Listbox(entryFrame)
entryList.pack()

# an entry widget, where we'll put our values
entryEntry = Tkinter.Entry(entryFrame)
entryEntry.pack()

# our button, which takes in our values
entryButton = Tkinter.Button(entryFrame, text="Submit")
entryButton.pack()

# a function to take from our entry and add to our values
def addToList():
    val = entryEntry.get()
    entryList.insert(entryList.size(), val)
    entryEntry.delete(0, len(val))

entryButton.config(command=addToList)

# our display frame, for our Bingo Board
displayFrame = Tkinter.Frame(top)
displayFrame.pack(side="right")

# let's add our tiles!
tiles = []
for i in range(5):
    for j in range(5):
        tiles.append(Tkinter.Button(displayFrame))
        tiles[len(tiles)-1].grid(row=i, column=j)

shuffleButton = Tkinter.Button(entryFrame, text="Shuffle")
shuffleButton.pack()

# import random to shuffle board values
import random
def setValues():
    values = list(entryList.get(0, entryList.size()))
    random.shuffle(values)
    for t in tiles:
        if len(values) != 0:
            val = values.pop()
            t.config(text=val)

shuffleButton.config(command=setValues)

if __name__ == '__main__':
    top.mainloop()
