#!/usr/bin/python           # This is server.py file

import socket, pickle                # Import socket module

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)      # Create a socket object
host = socket.gethostname() # Get local machine name
port = 5555                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

data = {1,2,3,4,5,6,7,8,9,10}

serial = pickle.dumps(data, protocol=0)


s.listen(5)                 # Now wait for client connection.
while True:
    c, addr = s.accept()     # Establish connection with client.
    print 'Got connection from', addr
    c.send(serial)
    c.close()                # Close the connection