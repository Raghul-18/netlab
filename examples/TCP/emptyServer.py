from twisted.internet import reactor, protocol

class echoServer(protocol.Protocol):

    def dataReceived(self, data):
        if self.transport.value():
            print("Data", data.decode())
            flag = "File Received"
            self.transport.write(flag.encode())
        else:
            print("Data", data.decode())
            flag = "Empty File Received"
            self.transport.write(flag.encode())

class echoFactory(protocol.Factory):

    def buildProtocol(self, addr):
        return echoServer()
    
reactor.listenTCP(7304, echoFactory())
reactor.run()