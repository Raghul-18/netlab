from twisted.internet import reactor, protocol

class echoServer(protocol.DatagramProtocol):

    def datagramReceived(self, datagram, addr):
        if datagram.decode() == "CL":
            print("Connection Lost!")
            self.transport.stopListening()
        else:
            print("Message from Client -", datagram.decode())

reactor.listenUDP(8036, echoServer())
reactor.run()