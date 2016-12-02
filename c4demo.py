from c4_lib import c4_io, c4_engine
from c4_gui import pygameGUI#, menu_gui
import getopt
import sys
import random, copy, sys, pygame
from pygame.locals import *

def main():
    game = c4_engine.Game(6, 7, 4)
    gui = pygameGUI.Gui()
    playerOne = 0
    playerTwo = 1
    # Set up a blank board data structure.
    turn = playerOne
    showHelp = True
    while True:  # main game loop
        if turn == playerOne:
            print 'hi'
            # Human player's turn.
            column = gui.getPlayerMove(game.board, showHelp)
            gui.animateDroppingToken(game.board, column, 0)
            game.place_token(turn, column)
            gui.drawBoard(game.board)
            pygame.display.update()
            if showHelp:
                # turn off help arrow after the first move
                showHelp = False
            if game.check_winner() != -1:
                print 'oops'
                winnerImg = gui.HUMANWINNERIMG
                gui.mainLoop(game.board, gui.HUMANWINNERIMG)
                break
            turn = playerTwo  # switch to other player's turn
        else:
            print 'fish'
            if showHelp:
                # turn off help arrow after the first move
                showHelp = False
            if game.check_winner() != -1:
                winnerImg = gui.HUMANWINNERIMG
                gui.mainLoop(game.board, gui.HUMANWINNERIMG)
                break
            turn = playerOne  # switch to other player's turn

        if game.check_full_board():
            # A completely filled board means it's a tie.
            winnerImg = gui.TIEWINNERIMG
            break
        # game.print_formated()

    # # Start the game loop.
    # while (1):
    #     print "Enter Column # to Place Token or type save to Save your current game:"
    #     pos = raw_input("Col # or save: ")
    #     if pos.lower() == "save":
    #         print "Saving game..."
    #         if io.save_obj(game, "game.txt", "w"):
    #             print "Game Saved Successfully!"
    #             continue
    #         else:
    #             print "An error occured, Please try Again"
    #             continue
    #
    #     # Check for valid col input
    #     try:
    #         if pos.isdigit() and int(pos) >= 0 and int(pos) < width:
    #             pos = int(pos)
    #         else:
    #             print "The Column you entered is invalid. Please try again."
    #             continue
    #     except AttributeError as e:
    #         print "You did not specify a number parameter. Please try again."
    #         print e
    #         sys.exit(2)
    #
    #     # Check place token returns false, the col is full
    #     if not game.place_token(player, pos):
    #         print "This column is already full. Try again."
    #         continue
    #
    #     print "**********************"
    #     print "    Board Updated     "
    #     print "**********************"
    #     game.print_formated()
    #     print "\n"
    #
    #     # Check for full board at the end of every insertion
    #     if game.check_full_board():
    #         print "This game is a tie. Thanks for playing!"
    #         break
    #
    #     # Check winning conditions. Break out of game loop if winner is found
    #     if game.check_winner() != -1:
    #         print "Player " + str(game.check_winner()) + " has Won the game!. Thanks for playing!"
    #         break
    #
    #     # Toggle player value at end of round
    #     if player == 1:
    #         player = 0
    #     else:
    #         player = 1
    #
    #     # Update the user with the current player
    #     print "Player " + str(player) + "s turn..."


if __name__ == "__main__":
    main()