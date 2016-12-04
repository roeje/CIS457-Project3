
#!/usr/bin/python           # This is server.py file

import socket               # Import socket module
import threading

def main():
    server_data = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a socket object
    server_msg = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    host = socket.gethostname()  # Get local machine name
    data_port = 55555  # Reserve a port for your service.
    msg_port = 55556

    server_data.bind((host, data_port))  # Bind to the port
    server_msg.bind((host, msg_port))

    print 'Sockets Created, waiting for connections...'

    server_data.listen(5)

    data, addr = server_data.accept()

    print 'Connection made'

if __name__ == "__main__":
    main()
