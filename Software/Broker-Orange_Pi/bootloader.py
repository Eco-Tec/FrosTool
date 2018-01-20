from socket import socket, error


class Bootloader():
    def __init__(self, ip= "192.168.43.176", port = 65):
        self.sock = socket()
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
        self.sock.listen(0)
        print("Esperando conexion ....")
        self.conn, self.addr = self.sock.accept()
        print("Conexion aceptada....")
        self.send_file("/home/game/plantilla.txt")

    def send_file(self, name):
        self.file = open(name, "r")
        m = self.file.readline()
        while m != "":
            print(m)
            msg = 'Thank you for connecting'+ "\r\n"
            self.sock.send(msg.encode('ascii'))
            m = self.file.readline()
            print(m)
        self.file.close()
        self.sock.send(END_FILE,"utf-8")
        self.sock.close()
