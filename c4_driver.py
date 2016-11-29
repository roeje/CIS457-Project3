from c4_lib import c4_io, c4_engine
import getopt
import sys
import re

# Main method that implements the terminal interface to play game
# To run call file with parameters(ex): python c4_driver.py -h4 -w5 -r3
# the -l argument can be added to automatically load game if it exists
def main (argv) :

    height = 0
    width = 0
    win_len = 0
    load_game = False
    io = c4_io.IO()
    player = 0

    # Parse parameters from command line
    try:
        # h = height, w = width, r = length to win, l is flag for automatic load
        opts, args = getopt.getopt(argv, "h:w:r:l")
    except getopt.GetoptError:
        print "Parameters were missing. Please provide: -h height, -w width, -r row length. Add -l if you would like to load a saved game"
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            height = arg
        elif opt == "-w":
            width = arg
        elif opt == "-r":
            win_len = arg
        elif opt == "-l":
            load_game = True

    # Error check for all parameters
    try:
        if height.isdigit() and width.isdigit() and win_len.isdigit():
            height = int(height)
            width = int(width)
            win_len = int(win_len)
        else:
            raise ValueError("An input was not in integer format. Please make sure your inputs are numbers.")

    except ValueError as e:
        print e
        sys.exit(2)
    except AttributeError as e:
        print "You did not specify any parameter. Please try again."
        print e
        sys.exit(2)

    try:
        if height >= 2 and width >= 2:
            print
        else:
            raise ValueError("The parameters you enter are too small. Please enter a hight and with greater than 2.")
    except ValueError as e:
        print e
        sys.exit(2)

    try:
        if win_len > 0:
            print
        else:
            raise ValueError("Your length to win was too small. Please enter an winning length greater than 0")
    except ValueError as e:
        print e
        sys.exit(2)

    # Create new game object based on parameters
    game = c4_engine.Game(height, width, win_len)

    # Begining Game
    print "***** Starting Connect 4: *****\n"

    # Check for loadgame conditions
    if not load_game:
        print "Would you like to try to load a previous game?"
        answer = raw_input("yes or no: ")
    else:
        answer = ""

    if answer.lower() == "yes" or load_game:
        print "Checking for previous game..."
        result = io.load_obj("game.txt")
        if result:
            game = result
            print "Board Loaded!"
        else:
            print "Game could not be loaded. Starting a new game..."


    print "*****************************************"
    print "Player " + str(player) + "s Turn:"

    game.print_formated()

    # Start the game loop.
    while(1):
        print "Enter Column # to Place Token or type save to Save your current game:"
        pos = raw_input("Col # or save: ")
        if pos.lower() == "save":
            print "Saving game..."
            if io.save_obj(game, "game.txt", "w"):
                print "Game Saved Successfully!"
                continue
            else:
                print "An error occured, Please try Again"
                continue

        # Check for valid col input
        try:
            if pos.isdigit() and int(pos) >= 0 and int(pos) < width:
                pos = int(pos)
            else:
                print "The Column you entered is invalid. Please try again."
                continue
        except AttributeError as e:
            print "You did not specify a number parameter. Please try again."
            print e
            sys.exit(2)

        # Check place token returns false, the col is full
        if not game.place_token(player, pos):
            print "This column is already full. Try again."
            continue

        print "**********************"
        print "    Board Updated     "
        print "**********************"
        game.print_formated()
        print "\n"

        # Check for full board at the end of every insertion
        if game.check_full_board():
            print "This game is a tie. Thanks for playing!"
            break

        # Check winning conditions. Break out of game loop if winner is found
        if game.check_winner() != -1:
            print "Player " + str(game.check_winner()) + " has Won the game!. Thanks for playing!"
            break

        # Toggle player value at end of round
        if player == 1:
            player = 0
        else:
            player = 1

        # Update the user with the current player
        print "Player " + str(player) + "s turn..."

if __name__ == "__main__":
    main(sys.argv[1:])