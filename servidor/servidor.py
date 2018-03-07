import socketserver, threading, time
import socket

HOST, PORT = "172.24.43.158", 8090
host_name = "Host name: %s" % socket.gethostname()
ipAddress= "IP address: %s" % socket.getaddrinfo(HOST,PORT)
numeroDeClientes = 0

class ThreadedUDPRequestHandler(socketserver.BaseRequestHandler):
    def handle(self):
        global numeroDeClientes

        data = self.request[0].strip()
        opcion= data[0]
        socket = self.request[1]
        current_thread = threading.current_thread()

        if (opcion == 48): # 0 inicializar
            numeroDeClientes += 1
            print("{}: client: {}, wrote: {}".format(current_thread.name, self.client_address,
                                                     "Nuevo Cliente # "+ str(numeroDeClientes)))
            socket.sendto(host_name.encode(), self.client_address)

        elif (opcion == 49): #1
            socket.sendto(host_name.encode(), self.client_address)

        elif (opcion== 50): #2
            socket.sendto(ipAddress.encode(), self.client_address)

        elif (opcion== 51): #3
            socket.sendto(ipAddress.encode(), self.client_address)

        elif (opcion== 52): #4
            socket.sendto(ipAddress.encode(), self.client_address)

        elif (opcion== 53): #5
            socket.sendto(ipAddress.encode(), self.client_address)

        elif (opcion== 54): #6
            print(numeroDeClientes)
            numeroDeClientes -= 1
            mensaje= "Cliente desactivado"
            socket.sendto(mensaje.encode(), self.client_address)

        else:
            socket.sendto(data.upper(), self.client_address)


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