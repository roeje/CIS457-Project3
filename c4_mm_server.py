
#!/usr/bin/python           # This is server.py file

import socket, pickle               # Import socket module
import threading
from SocketServer import ThreadingMixIn


class ClientThread(threading.Thread):
    def __init__(self, ip, port, db):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.database = db
        print "[+] New server socket thread started for " + ip + ":" + str(port)

    def run(self):
        while True:
            cmd = conn.recv(100)
            print "Server received data: " + cmd

            if (cmd.lower() == 'start'):
                print 'Sending Test to client'

            if (cmd.lower() == 'removeuser'):
                print 'Removing user'
                username = server_data.recv(1024)

                tmp = None
                for game in self.database:
                    if game[0] == username:
                        tmp = game

                self.database.remove(tmp)
                print self.database
                print 'User: ' + username + ' removed from database'

            if (cmd.lower() == 'getusers'):
                print 'Get users request'
                threadLock.acquire()
                userlist = pickle.dumps(self.database)
                print userlist
                threadLock.release()
                conn.send(userlist)
                print 'Users successfully sent'

            if (cmd.lower() == 'postusers'):
                print 'posting user information'
                data = conn.recv(1024).split('/')

                print data[0]
                print data[1]

                self.database.append((data[0], data[1]))
                print 'data successfully inserted'
                print self.database


server_data = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a socket object
server_data.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
host = socket.gethostname()  # Get local machine name
print host
data_port = 55555  # Reserve a port for your service.
threadLock = threading.Lock()
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
