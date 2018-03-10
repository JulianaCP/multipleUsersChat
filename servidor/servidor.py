import socketserver, threading, time
import socket
import urllib.request
import json
import datetime

HOST, PORT = "172.24.73.178", 9090
host_name = "Host name: %s" % socket.gethostname()
ipAddress= "IP address: %s" % socket.getaddrinfo(HOST,PORT)
numeroDeDatos = 0


class ThreadedUDPRequestHandler(socketserver.BaseRequestHandler):
    def handle(self):
        global numeroDeDatos
        data = self.request[0].strip()
        socket = self.request[1]
        number,code = data.decode().split(",")
        print(number)
        print(code)
        current_thread = threading.current_thread()
        print("{}: client: {}, wrote: {}".format(current_thread.name, self.client_address, data))
        numeroDeDatos += 1
        if (number == "1"): #1
            socket.sendto(host_name.encode(), self.client_address)
        elif (number == "2"): #2
            socket.sendto(ipAddress.encode(), self.client_address)
        elif (number == "3"): #3
            datos= str(numeroDeDatos)
            socket.sendto(datos.encode(), self.client_address)
        elif (number == "4"):
            contents = urllib.request.urlopen(
                "http://api.timezonedb.com/v2/list-time-zone?key=6I35P7039N8L&format=json&country="+code).read().decode(
                'utf8')
            wjdata = json.loads(contents)
            unix_time = wjdata['zones'][0]['timestamp']
            variable = datetime.datetime.utcfromtimestamp(
                int(unix_time)
            ).strftime('%Y-%m-%d %H:%M:%S')
            print(variable)
            socket.sendto(variable.encode(), self.client_address)
        elif (number == "5"):
            socket.sendto("Hola! el servidor esta feliz de verte".encode(), self.client_address)
        numeroDeDatos -= 1

class ThreadedUDPServer(socketserver.ThreadingMixIn, socketserver.UDPServer):
    pass

if __name__ == "__main__":
    server = ThreadedUDPServer((HOST, PORT), ThreadedUDPRequestHandler)
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True
    print("Host name: %s" % host_name)
    try:
        server_thread.start()
        print("Server started at {} port {}".format(HOST, PORT))
        while True: time.sleep(100)
    except (KeyboardInterrupt, SystemExit):
        server.shutdown()
        server.server_close()
        exit()