#!/usr/bin/python           # This is server.py file
import socket
from threading import Thread
from c4_gui import menu_gui
import c4_client as c
import c4_server as s

server_data = None
def main():
    server_data = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a socket object
    server_msg = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    host = socket.gethostname()  # Get local machine name
    data_port = 55555  # Reserve a port for your service.
    msg_port = 55556

    server_data.connect((host, data_port))  # Bind to the port
    # server_msg.connect((host, msg_port))

    server_data.send("Connection Successful...")




    data = server_data.recv(1024)
    print " Client2 received data:", data

def startup():
    commandNotFound = True
    while commandNotFound:
        command = raw_input("Type 'create' to create a game or 'join' to join a game")
        if command.lower() == "create":
            start_server()
            commandNotFound = False
        elif command.lower() == "join":
            list_games()

def list_games():
    game_list = server_data.recieve(1024)

    count = 1
    for game in game_list:
        print "Game No: ", count, "  Username: ", game[0], "  IP Adress: ", game[1]

    validGame = False
    selected_game = None
    while not validGame:
        gameNumString = raw_input("Enter the number of the game you wish to join.")
        try:
            gameNum = int(gameNumString)
        except ValueError:
            print 'Please enter an integer'

        gameNum = gameNum - 1
        if gameNum >= 0 and gameNum < game_list.length:
            selected_game = game_list[gameNum]
            validGame = True
        else:
            print "Please choose a number that is in the list of games."

    create_client_game(selected_game[1])
            

def start_server():
    print '******************** Starting C4 Server ********************\n'
    username = raw_input('Enter a username: ')
    print 'Game Published to Match Making Server\n'
    print 'Starting Game...'
    create_server_game()

def post_game(username):

    return

def create_client_game(host):

    thread2 = c.Client(host)
    thread2.start()
    return

def create_server_game():
    thread3 = s.Server()
    thread3.start()
    return

if __name__ == "__main__":
    main()
