
#!/usr/bin/python           # This is server.py file

import socket, pickle               # Import socket module
from threading import Thread
from SocketServer import ThreadingMixIn


class ClientThread(Thread):
    def __init__(self, ip, port, db):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.database = db
        print "[+] New server socket thread started for " + ip + ":" + str(port)

    def run(self):
        while True:
            cmd = conn.recv(2048)
            print "Server received data:", cmd
            if (cmd.lower == 'start'):
                conn.send('Test Recieved')


            if (cmd.lower == 'getusers'):
                userlist = pickle.dumps(self.database)
                conn.send(userlist)

            if (cmd.lower == 'postusers'):
                username = conn.recv(1024)
                hostname = conn.recv(1024)
                self.database.append((username, hostname))


server_data = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a socket object
server_data.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
host = socket.gethostname()  # Get local machine name
data_port = 55555  # Reserve a port for your service.
threads = []
datalist = []
server_data.bind((host, data_port))  # Bind to the port
print 'Sockets Created, waiting for connections...'

while True:
    server_data.listen(5)
    print "Multithreaded Python server : Waiting for connections from TCP clients..."
    (conn, (ip, port)) = server_data.accept()
    print 'Connection made'
    newthread = ClientThread(ip, port, datalist)
    newthread.start()
    threads.append(newthread)


for t in threads:
    t.join()
