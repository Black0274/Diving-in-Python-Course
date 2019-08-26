import socket
import time
import json


class ClientError(Exception):
    def __init__(self, text):
        self.txt = text


class Client:

    def __init__(self, host, port, timeout=None):
        self.host = host
        self.port = port
        self.timeout = timeout
        # self.connected = False
        self.sock = socket.socket()
        self.connect()

    def connect(self):
        try:
            self.sock = socket.create_connection((self.host, self.port), self.timeout)
            print("connection established")
        except ConnectionRefusedError:
            pass
            # print("connection failed")
        except socket.timeout:
            print("connection failed: timeout")
        except socket.error as ex:
            print("connection failed: ", ex)

    def put(self, key, value, timestamp=int(time.time())):
        try:
            # if not self.connected:
            #    self.connect()
            #   self.connected = True
            self.sock.sendall(str.encode("put " + key + " " + str(value) + " " + str(timestamp) + "\n"))
            recv = self.sock.recv(1024)
            if recv == "error\nwrong command\n\n":
                raise ClientError("entered wrong command")
        except socket.error as ex:
            raise ClientError(ex)

    def get(self, key):
        mdict = {}
        try:
            self.sock.sendall(("get " + key + "\n").encode("utf8"))
            data = self.sock.recv(1024)
            if data == b"ok\n\n":
                return mdict
            mdict = self.parse(data.decode("utf8"))
            return mdict
        except socket.error as ex:
            raise ClientError(ex)
        except IndexError as ex:
            raise ClientError(ex)

    @staticmethod
    def parse(str):
        spl = str.split("\n")[1:-2]
        mdict = {}
        for line in spl:
            line = line.split()
            if mdict.get(line[0]):
                mdict[line[0]].append((int(line[2]), float(line[1])))
            else:
                mdict[line[0]] = [(int(line[2]), float(line[1]))]
        return mdict

client = Client("127.0.0.1", 10000, timeout=5)
client.put("test", 0.5, timestamp=1)
client.put("test", 2.0, timestamp=2)
client.put("test", 0.5, timestamp=3)
client.put("load", 3, timestamp=4)
client.put("load", 4, timestamp=5)
print(client.get("test"))
# md = {}
# print(client.get("*"))
# print(md.get(13))
# print(type(Client("127.0.0.1", 10000, timeout=2)))
# client.put("palm.cpu", 0.5)
