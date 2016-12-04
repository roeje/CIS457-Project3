#!/usr/bin/python           # This is server.py file
import socket
from c4_gui import menu_gui
import c4_client as c


def main():
    server_data = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a socket object
    server_msg = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    host = socket.gethostname()  # Get local machine name
    data_port = 55555  # Reserve a port for your service.
    msg_port = 55556

    server_data.connect((host, data_port))  # Bind to the port
    # server_msg.connect((host, msg_port))

    gui = menu_gui.MainGui(create_server_game, create_client_game)
    gui.run()


def create_client_game(host):
    client = c.Client(host)
    # client.run()
    return


def create_server_game():
    return


if __name__ == "__main__":
    main()
