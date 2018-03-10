import socketserver, threading, time
import socket

HOST, PORT = "172.24.43.158", 8090
host_name = "Host name: %s" % socket.gethostname()
ipAddress= "IP address: %s" % socket.getaddrinfo(HOST,PORT)
numeroDeDatos = 0


class ThreadedUDPRequestHandler(socketserver.BaseRequestHandler):
    def handle(self):
        global numeroDeDatos
        data = self.request[0].strip()
        opcion= data[0]
        socket = self.request[1]
        current_thread = threading.current_thread()
        print("{}: client: {}, wrote: {}".format(current_thread.name, self.client_address, data))

        numeroDeDatos += 1

        if (opcion == 49): #1
            socket.sendto(host_name.encode(), self.client_address)
        elif (opcion == 50): #2
            socket.sendto(ipAddress.encode(), self.client_address)
        elif (opcion == 51): #3
            datos= str(numeroDeDatos)
            socket.sendto(datos.encode(), self.client_address)
        else:
            socket.sendto(host_name.encode(), self.client_address)
            socket.sendto(data.upper(), self.client_address)

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