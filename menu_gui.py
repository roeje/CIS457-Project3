import Tkinter
from Tkinter import *

class Menu:

    def __init__(self, menuListener):
        self.menuListener = menuListener
        self.root = Tk()
        self.frame = Frame(self.root)

        self.bottomframe = Frame(self.root, height=480, width=640)

        self.frame.pack()
        self.bottomframe.pack( side = BOTTOM )

        self.createButton = Button(self.frame, text="Create a Game", fg="red", width = 60, height = 2, command = self.create_game)
        self.createButton.pack(side = LEFT)

        self.joinButton = Button(self.frame, text="Join a Game", fg="blue", width = 60, height = 2, command = self.join_game)
        self.joinButton.pack(side = RIGHT)

        self.messageBox = Text(self.bottomframe, height=5, width=101)
        self.messageBox.pack(side = LEFT, expand=2)

        self.messageButton = Button(self.bottomframe, text ="send", fg="#26e038", command = self.send_message, height = 5, width = 6)
        self.messageButton.pack(side=RIGHT, expand = 2)
        self.root.mainloop()

    def send_message(self):
        self.messageText = self.messageBox.get("1.0", END)
        print self.messageText

    def create_game(self):
        self.menuListener.__call__()

    def join_game(self):
        print 'join'
