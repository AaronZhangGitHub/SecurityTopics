import sys
import socket

def main():
    HOST = 'localhost'
    PORT = int(sys.argv[1])
    sendFilePath = sys.argv[2] #File to send to Bob
    saveFilePath = sys.argv[3] #Path that is saved on Bobs machine
    client = clientTCPHandler(HOST,PORT,sendFilePath,saveFilePath)
    client.connect
    x = str.encode("hello")
    client.send(x)
class clientTCPHandler():
    def __init__(self,host,port,fileToSendPath, targetPath):
        self.host = host
        self.port = port
        self.fileToSendPath = fileToSendPath
        self.targetPath = targetPath
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    def connect(self):
        print("Connecting ")
        self.sock.connect((host,port))
    def send(self, message):
        self.sock.send(message)
main()
