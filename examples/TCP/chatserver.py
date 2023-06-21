from __future__ import print_function
from twisted.internet import protocol
from twisted.protocols import basic
from twisted.application import service, internet

class Chat(basic.LineReceiver):
    
    clients = []

    def connectionMade(self):
        self.client_id = len(self.factory.clients) + 1
        print("Client{} Connected!".format(self.client_id))
        self.factory.clients.append(self)

    def connectionLost(self, reason):
        print("Client{} Disconnected!".format(self.client_id))
        self.factory.clients.remove(self)

    def lineReceived(self, line):
        print("Client{} - {}".format(self.client_id, line.decode()))
        for client in self.factory.clients:
            if client != self:
                client.sendLine(("Client{} - {}".format(self.client_id, line.decode())).encode())

    def message(self, message):
        self.sendLine(message.encode())

factory = protocol.ServerFactory()
factory.protocol = Chat()

application = service.Application("chatserver")
internet.TCPServer(1025, factory).setServiceParent(application)