#!/usr/bin/python           # This is server.py file

from c4_lib import c4_io, c4_engine
from c4_gui import pygameGUI#, menu_gui
import getopt
import sys
import random, copy, sys, pygame
from pygame.locals import *
from random import randint
import socket, pickle                # Import socket module


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a socket object
    host = socket.gethostname()  # Get local machine name
    port = 5555  # Reserve a port for your service.
    s.connect((host, port))

    print 'Connected to server'

    game = c4_engine.Game(6, 7, 4)
    gui = pygameGUI.Gui(6, 7)
    playerOne = 0
    playerTwo = 1

    # game.print_formated()

    turn = playerOne
    showHelp = True

    gui.drawBoard(game.board)
    gui.display_update()

    while True:  # main game loop
        if turn == playerOne:
            print 'Player Two Turn:'

            # Get other player's move
            column = int(s.recv(1024))

            gui.animateDroppingToken(game.board, column, 'black')
            game.place_token(turn, column)
            gui.drawBoard(game.board)
            gui.display_update()
            if game.check_winner() == playerOne:
                print 'Winner Found: Player One'
                winnerImg = gui.HUMANWINNERIMG
                gui.mainLoop(game.board, gui.HUMANWINNERIMG)
                break
            turn = playerTwo  # switch to other player's turn
        else:
            print 'Player One Turn:'

            column = gui.getPlayerMove(game.board, showHelp)
            gui.animateDroppingToken(game.board, column, 'red')
            game.place_token(turn, column)
            gui.drawBoard(game.board)
            gui.display_update()

            # Send move to playerOne
            s.send(str(column))

            if showHelp:
                # turn off help arrow after the first move
                showHelp = False
            if game.check_winner() == playerTwo:
                print 'Winner Found: Player Two'
                winnerImg = gui.HUMANWINNERIMG
                gui.mainLoop(game.board, gui.HUMANWINNERIMG)
                break
            turn = playerOne  # switch to other player's turn

        if game.check_full_board():

            winnerImg = gui.TIEWINNERIMG
            break

    s.close()

if __name__ == "__main__":
    main()
