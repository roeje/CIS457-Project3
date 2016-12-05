import Tkinter
from Tkinter import *
from threading import Thread
import socket

class MainGui(Thread):
    root = Tk()
    frame = Frame(root)
    messageBox = None

    bottomframe = Frame(root, height=100, width=640)

    send_message = None
    build_server = None

    def __init__(self, server_func, client_func):
        Thread.__init__(self)
        self.build_client = client_func
        self.build_server = server_func
        self.run()

    def send_message(self):
        self.messageText = self.messageBox.get("1.0", END)
        print self.messageText

    def create_game(self):
        print 'game'
        self.build_server()

    def join_game(self):
        print 'join'
        self.build_client(socket.gethostname())

    def run(self):
        self.frame.pack()
        self.bottomframe.pack( side = BOTTOM )

        createButton = Button(self.frame, text="Create a Game", fg="red", width = 60, height = 2, command = self.create_game)
        createButton.pack(side = LEFT)

        joinButton = Button(self.frame, text="Join a Game", fg="blue", width = 60, height = 2, command = self.join_game)
        joinButton.pack(side = RIGHT)

        self.messageBox = Text(self.bottomframe, height=5, width=101)
        self.messageBox.pack(side = LEFT, expand=2)

        messageButton = Button(self.bottomframe, text ="send", fg="#26e038", command = self.send_message, height = 5, width = 6)
        messageButton.pack(side=RIGHT, expand = 2)
        self.root.mainloop()
