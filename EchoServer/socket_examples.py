#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import atexit
from net.Socket import SocketServer

server = SocketServer(port=8009)

def shutdownServer():
    server.shutdown()

atexit.register(shutdownServer)

def onMessage(clientAddress, connection, data):  # @UnusedVariable
    # print ("Got data from client " + str(clientAddress) + " --> " + data)
    server.send(connection, data)
    
server.onMessageCallback(onMessage)
    
server.start();

print "Server started!!!"

def keepAlive():
    while 1:
        time.sleep(0.1)

keepAlive()