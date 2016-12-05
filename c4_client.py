#!/usr/bin/python           # This is server.py file

from c4_lib import c4_io, c4_engine
from c4_gui import pygameGUI#, menu_gui
import getopt
import sys
import random, copy, sys, pygame
from pygame.locals import *
from random import randint
import socket, pickle                # Import socket module
from threading import Thread


class Client(Thread):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = 0
    port = 5555

    game = None
    gui = None
    playerOne = 0
    playerTwo = 1
    turn = playerOne
    showHelp = True

    def __init__(self, host):
        Thread.__init__(self)
        self.host = host  # Get local machine name
        self.s.connect((host, self.port))

        print 'Connected to server'

        self.game = c4_engine.Game(6, 7, 4)
        self.gui = pygameGUI.Gui(6, 7)

        self.gui.drawBoard(self.game.board)
        self.gui.display_update()
        self.run()

    def run(self):

        while True:  # main game loop
            if self.turn == self.playerOne:
                print 'Player Two Turn:'

                # Get other player's move
                column = int(self.s.recv(1024))
                col = self.game.check_for_col_height(column)

                self.gui.animateDroppingToken(self.game.board, column, 'red', col)
                self.game.place_token(self.turn, column)
                self.gui.drawBoard(self.game.board)
                self.gui.display_update()
                if self.game.check_winner() == self.playerOne:
                    print 'Winner Found: Player One'
                    winnerImg = self.gui.HUMANWINNERIMG
                    self.gui.mainLoop(self.game.board, self.gui.HUMANWINNERIMG)
                    break
                self.turn = self.playerTwo  # switch to other player's turn
            else:
                print 'Player One Turn:'

                column = self.gui.getPlayerMove(self.game.board, self.showHelp)

                if self.game.check_for_col_height(column) != -1:
                    col = self.game.check_for_col_height(column)
                    self.gui.animateDroppingToken(self.game.board, column, 'black', col)
                    self.game.place_token(self.turn, column)
                else:
                    print 'Col #' + str(column) + ' is full... breaking'
                    self.gui.drawBoard(self.game.board)
                    self.gui.display_update()
                    break

                self.gui.drawBoard(self.game.board)
                self.gui.display_update()

                # Send move to playerOne
                self.s.send(str(column))

                if self.showHelp:
                    # turn off help arrow after the first move
                    self.showHelp = False
                if self.game.check_winner() == self.playerTwo:
                    print 'Winner Found: Player Two'
                    winnerImg = self.gui.HUMANWINNERIMG
                    self.gui.mainLoop(self.game.board, self.gui.HUMANWINNERIMG)
                    break
                self.turn = self.playerOne  # switch to other player's turn

            if self.game.check_full_board():

                winnerImg = self.gui.TIEWINNERIMG
                break

        self.s.close()
