#!/usr/bin/python           # This is server.py file
import socket
from threading import Thread
from c4_gui import menu_gui
import c4_client as c
import c4_server as s


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
    print

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
