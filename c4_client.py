#!/usr/bin/python           # This is client.py file

import socket, pickle              # Import socket module

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)        # Create a socket object
host = socket.gethostname() # Get local machine name
port = 5555                # Reserve a port for your service.

s.connect((host, port))
serial = s.recv(1024)
data = pickle.loads(serial)
print data
s.close                     # Close the socket when done
