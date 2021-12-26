import socket
from threading import Thread, Event

class SocketTCP:
    EVENT = 0
    RECEIVE = 1
    DISCONNECT = 2
    CONNECTED = 3
    _isConnect = False
    killEvent = Event()

    def __init__(self, host, port, bufSize=1024) -> None:
        self.host = host
        self.port = port
        self.bufSize = bufSize
    
    def connect(self):
        def job():
            self._server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self._server.bind((self.host, self.port))
            self._server.listen(5)
            self.client, self.addr = self._server.accept()
            self._isConnect = True
            self.listen(self.CONNECTED, None)
            while not self.killEvent.is_set():
                recv = self.client.recv(self.bufSize)
                if len(recv) > 0:
                    self.listen(self.RECEIVE, recv)
                else:
                    self.listen(self.DISCONNECT, None)
                    self._isConnect = False
                    return
        Thread(target=job).start()

    def set_listen(self, listen):
        self.listen = listen

    def send(self, msg):
        try:
            self.client.send(msg.encode())
            return True
        except ConnectionAbortedError:
            return False

    def close(self):
        self._isConnect = False
        self.client.close()
        self.killEvent.set()
    
    def isConnect(self):
        return self._isConnect
    
    def waitConnect(self):
        while not self.isConnect():
            pass