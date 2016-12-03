from c4_lib import c4_io, c4_engine
from c4_gui import pygameGUI#, menu_gui
import getopt
import sys
import random, copy, sys, pygame
from pygame.locals import *

def main():
    game = c4_engine.Game(6, 7, 4)
    gui = pygameGUI.Gui(6, 7)
    playerOne = 0
    playerTwo = 1

    # game.print_formated()

    turn = playerOne
    showHelp = True

    while True:  # main game loop
        if turn == playerOne:
            print 'Player One Turn:'

            column = gui.getPlayerMove(game.board, showHelp)
            gui.animateDroppingToken(game.board, column, 'red')
            game.place_token(turn, column)
            gui.drawBoard(game.board)
            gui.display_update()
            if showHelp:
                # turn off help arrow after the first move
                showHelp = False
            if game.check_winner() == playerOne:
                print 'Winner Found: Player One'
                winnerImg = gui.HUMANWINNERIMG
                gui.mainLoop(game.board, gui.HUMANWINNERIMG)
                break
            turn = playerTwo  # switch to other player's turn
        else:
            print 'Player Two Turn:'
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


if __name__ == "__main__":
    main()
