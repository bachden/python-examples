import socket
import select
from threading import Thread
from concurrent.futures.thread import ThreadPoolExecutor

class SocketServer:
    socket = None
    callback = None
    acceptThread = None
    connections = {}
    clientAddresses = {}
    eventLoop = None
    executor = None
    
    def __init__(self, host="localhost", port=9000):
        self.host = host
        self.port = port
    
    def start(self): 
        print ("Start listening on " + self.host + ":" + str(self.port))
        
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serverAddress = (self.host, self.port)
        self.socket.bind(serverAddress)
        self.socket.setblocking(False)
        self.socket.settimeout(3600)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.listen(10000)
        
        def acceptNewConnection():
            print "Waiting for connection...\n"
            while True:
                connection, clientAddress = self.socket.accept()     
                self.connections[clientAddress] = connection
                self.clientAddresses[connection] = clientAddress
                print("New connection established from " + clientAddress[0] + ":" + str(clientAddress[1]))
        
        self.executor = ThreadPoolExecutor(max_workers=8)
        def loopForData():
            print "Looping for data\n"
            while True:
                readList, writeList, errList = select.select(self.connections.values(), [], [], 0.01)  # @UnusedVariable
                if len(readList) > 0:
                    for connection in readList:
                        data = connection.recv(1024)
                        if data and self.callback:
                            self.executor.submit(self.callback, self.clientAddresses[connection], connection, data)

        # start accept thread and event loop thread
        self.acceptThread = Thread(target=acceptNewConnection, args=())
        self.eventLoop = Thread(target=loopForData, args=())
        
        self.eventLoop.start()
        self.acceptThread.start()
        
    def send(self, connection, data):
        connection.sendall(data)
    
    def shutdown(self):
        if self.socket != None :
            self.socket.close()
            
    def onMessageCallback(self, callback):
        self.callback = callback
