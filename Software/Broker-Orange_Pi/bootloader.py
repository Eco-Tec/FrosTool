#from socket import socket, error

try:
    import usocket as socket
except ImportError:
    import socket
#import websocket_helper


class Bootloader():
    def __init__(self, ip= "192.168.31.166", port = 92):
        self.sock = socket.socket()
        self.ip = ip
        self.port = port
        self.file = ""
        self.name = ""

    def set_ip(self, ip):
        self.ip = ip

    def set_port(self, port):
        self.port = port

    def set_file(self, name):
        self.name = name

    def state(self):
        self.sock.bind((self.ip, self.port))
        self.sock.listen(1)
        print("Esperando conexion ....")
        self.conn, self.addr = self.sock.accept()
        print("Conexion aceptada....")
        self.recivir()
        self.send_file("/home/game/plantilla.txt")
        
    
    def recivir(self):
        #while True:
        print(self.conn.recv(2))
                  

    def send_file(self, name):
        self.file = open(name, "r")
        m = self.file.readline()
        while m != "":
            print(m)
            #msg = 'Thank you for connecting'+ "\r\n"
            self.conn.send(m.encode())
            m = self.file.readline()
        self.file.close()
        self.conn.send("END_FILE\n".encode())
        self.sock.close()
