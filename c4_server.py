#!/usr/bin/python

from c4_lib import c4_engine
from c4_gui import pygameGUI
from threading import Thread
import socket # Import socket module

class Server(Thread):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a socket object
    host = socket.gethostname()  # Get local machine name
    port = 5555  # Reserve a port for your service.
    c = None
    addr = None

    playerOne = 0
    playerTwo = 1

    turn = playerOne
    showHelp = True

    def __init__(self):
        Thread.__init__(self)
        self.s.bind((self.host, self.port))  # Bind to the port

        self.game = c4_engine.Game(6, 7, 4)
        self.gui = pygameGUI.Gui(6, 7)

        self.gui.drawBoard(self.game.board)
        self.gui.display_update()

        self.s.listen(5)  # Now wait for client connection.

        print 'Server created, waiting for connection...'

        self.c, self.addr = self.s.accept()  # Establish connection with client.
        print 'Got connection from', self.addr
        self.run()

    def run(self):
        while True:  # main game loop
            if self.turn == self.playerOne:
                print 'Player One Turn:'

                column = self.gui.getPlayerMove(self.game.board, self.showHelp)
                if self.game.check_for_col_height(column) != -1:
                    print 'Col #' + str(column) + ' is not full'
                    self.gui.animateDroppingToken(self.game.board, column, 'red')
                    self.game.place_token(self.turn, column)
                    # self.gui.drawBoard(self.game.board)
                    # self.gui.display_update()
                else:
                    print 'Col #' + str(column) + ' is full... breaking'
                    self.gui.drawBoard(self.game.board)
                    self.gui.display_update()
                    break

                self.gui.drawBoard(self.game.board)
                self.gui.display_update()

                # Send move to other player
                self.c.send(str(column))

                if self.showHelp:
                    # turn off help arrow after the first move
                    self.showHelp = False
                if self.game.check_winner() == self.playerOne:
                    print 'Winner Found: Player One'
                    winnerImg = self.gui.HUMANWINNERIMG
                    self.gui.mainLoop(self.game.board, self.gui.HUMANWINNERIMG)
                    break
                self.turn = self.playerTwo  # switch to other player's turn
            else:
                print 'Player Two Turn:'

                # Get other player's move
                column = int(self.c.recv(1024))

                self.gui.animateDroppingToken(self.game.board, column, 'black')
                self.game.place_token(self.turn, column)
                self.gui.drawBoard(self.game.board)
                self.gui.display_update()
                if self.game.check_winner() == self.playerTwo:

                    print 'Winner Found: Player Two'
                    winnerImg = self.gui.HUMANWINNERIMG
                    self.gui.mainLoop(self.game.board, self.gui.HUMANWINNERIMG)
                    break
                self.turn = self.playerOne  # switch to other player's turn

            if self.game.check_full_board():


                winnerImg = self.gui.TIEWINNERIMG
                break

        self.c.close()
