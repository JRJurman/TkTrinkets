# create initial window
import Tkinter
top = Tkinter.Tk()
top.title("Bingo Builder")
# create entry frame, for hitting buttons
entryFrame = Tkinter.Frame(top)
entryFrame.grid(row=0, column=0)
# a simple label widget
entryLabel = Tkinter.Label(entryFrame, text="Entry")
entryLabel.grid(row=0, column=0)
# a simple list widget, makes the window a bit bigger too!
entryList = Tkinter.Listbox(entryFrame)
entryList.grid(row=1, column=0)
# an entry widget, where we'll put our values
entryEntry = Tkinter.Entry(entryFrame)
entryEntry.grid(row=2, column=0)
# a function to take from our entry and add to our values
def addToList():
    entryList.insert(entryList.size(), entryEntry.get())
    entryEntry.delete(0, len(entryEntry.get()))
# our button, which takes in our values
entryButton = Tkinter.Button(entryFrame, text="Submit", command=addToList)
entryButton.grid(row=3, column=0)
# our display frame, for our Bingo Board
displayFrame = Tkinter.Frame(top)
displayFrame.grid(row=0, column=1)
# let's add our tiles!
tiles = []
for i in range(5):
    for j in range(5):
        tiles.append(Tkinter.Button(displayFrame))
        tiles[len(tiles)-1].grid(row=i, column=j)
# import random to shuffle board values
import random
def setValues():
    values = list(entryList.get(0, entryList.size()))
    random.shuffle(values)
    for t in tiles:
        if len(values) != 0:
            t.config(text=values.pop())

shuffleButton = Tkinter.Button(entryFrame, text="Shuffle", command=setValues)
shuffleButton.grid(row=4, column=0)

if __name__ == '__main__':
    top.mainloop()
