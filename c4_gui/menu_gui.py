import Tkinter
from Tkinter import *

root = Tk()
frame = Frame(root)

bottomframe = Frame(root, height=480, width=640)
def send_message():
    messageText = messageBox.get("1.0", END)
    print messageText

def create_game():
    print 'game'

def join_game():
    print 'join'

frame.pack()
bottomframe.pack( side = BOTTOM )

createButton = Button(frame, text="Create a Game", fg="red", width = 60, height = 2, command = create_game)
createButton.pack(side = LEFT)

joinButton = Button(frame, text="Join a Game", fg="blue", width = 60, height = 2, command = join_game)
joinButton.pack(side = RIGHT)

messageBox = Text(bottomframe, height=5, width=101)
messageBox.pack(side = LEFT, expand=2)

messageButton = Button(bottomframe, text ="send", fg="#26e038", command = send_message, height = 5, width = 6)
messageButton.pack(side=RIGHT, expand = 2)
root.mainloop()
