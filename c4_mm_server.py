
#!/usr/bin/python           # This is server.py file

import socket               # Import socket module
from threading import Thread
from SocketServer import ThreadingMixIn


class ClientThread(Thread):
    def __init__(self, ip, port):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        print "[+] New server socket thread started for " + ip + ":" + str(port)

    def run(self):
        while True:
            data = conn.recv(2048)
            print "Server received data:", data
            MESSAGE = raw_input("Multithreaded Python server : Enter Response from Server/Enter exit:")
            if MESSAGE == 'exit':
                break
            conn.send(MESSAGE)  # echo

server_data = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a socket object
server_data.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
host = socket.gethostname()  # Get local machine name
data_port = 55555  # Reserve a port for your service.
threads = []
server_data.bind((host, data_port))  # Bind to the port
print 'Sockets Created, waiting for connections...'

while True:
    server_data.listen(5)
    print "Multithreaded Python server : Waiting for connections from TCP clients..."
    (conn, (ip, port)) = server_data.accept()
    print 'Connection made'
    newthread = ClientThread(ip, port)
    newthread.start()
    threads.append(newthread)

for t in threads:
    t.join()
