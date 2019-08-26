import asyncio

database = {}

def run_server(host, port):
    loop = asyncio.get_event_loop()
    coro = loop.create_server(
        Server, host, port
    )

    server = loop.run_until_complete(coro)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()


class Server(asyncio.Protocol):

    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data):
        try:
            message = data.decode().split()
            print(message)
            if message[0] == "put":
                self.put_handle(message[1], message[2], message[3])
            elif message[0] == "get":
                self.get_handle(message[1])
            else:
                self.send_error()
                print("-----data_receive1-----")
        except IndexError:
            self.send_error()
            print("-----data_receive2-----")

    def send_error(self):
        self.transport.write("error\nwrong command\n\n".encode())

    def send_message(self, text="ok\n\n"):
        self.transport.write(text.encode())

    def put_handle(self, key, value, timestamp):
        try:
            if database.get(key):
                if (float(value), int(timestamp)) not in database.get(key):
                    database[key].append((float(value), int(timestamp)))
            else:
                database[key] = [(float(value), int(timestamp))]
            self.send_message()
        except:
            self.send_error()
            print("-----put-----")

    def get_handle(self, key):
        try:
            print(database)
            message = "ok\n\n"
            if database.get(key):
                message = "ok\n"
                lst = database[key]
                for item in lst:
                    message += key + " " + str(item[0]) + " " + str(item[1]) + "\n"
                message += "\n"
            elif key == "*":
                message = "ok\n"
                for dkey, dvalue in database.items():
                    for item in dvalue:
                        print(dkey)
                        message += dkey + " " + str(item[0]) + " " + str(item[1]) + "\n"
                message += "\n"
            self.send_message(message)
        except IndexError as ex:
            self.send_error()
            print("-----get-----\n" + str(ex))


#run_server("127.0.0.1", 8888)
