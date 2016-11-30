
#!/usr/bin/python           # This is server.py file

import socket               # Import socket module
import threading

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serversocket.bind((socket.gethostname(), 5555))
#start listening on server socket
serversocket.listen(5)

while 1:
    #accept connections from outside
    (clientsocket, address) = serversocket.accept()
    #now do something with the clientsocket
    #in this case, we'll pretend this is a threaded server
    ct = client_thread(clientsocket)
    ct.run()