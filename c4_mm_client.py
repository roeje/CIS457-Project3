#!/usr/bin/python           # This is server.py file
import socket
from c4_gui import menu_gui


def main():


    server_data = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a socket object
    server_msg = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    host = socket.gethostname()  # Get local machine name
    data_port = 5555  # Reserve a port for your service.
    msg_port = 5556

    server_data.bind((host, data_port))  # Bind to the port
    server_msg.bind((host, msg_port))

    server_data.listen(5)


    data, addr = server_data.accept()

    gui = menu_gui.MainGui()

def create_client_game(host):


def create_server_game():


if __name__ == "__main__":
    main()
