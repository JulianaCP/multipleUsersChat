import socket
import sys

def menu():
    HOST, PORT = "172.24.43.158", 8090
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data= "0"
    sock.sendto(data.encode(), (HOST, PORT))
    received = sock.recv(1024)

    while(True):
        print("*************        MENU PRINCIPAL      *******************")
        data = input("1. Consultar el nombre del host del Servidor\n"
                    "2. Consultar la IP del Servidor\n"
                    "3. Consultar la cantidad de procesos ejecutandose en el servidor\n"
                    "4. Dar la hora en otro pais indicando el paıs\n"
                    "5. Poder enviar mensajes entre cliente y servidor\n"
                    "6. Salir\n"
                    "Opción: ")
        sock.sendto(data.encode(), (HOST, PORT))
        received = sock.recv(1024)
        print("************************************************************")
        print("Sent:     {}".format(data))
        print("Received: {}".format(received.decode()))
        print("************************************************************")
        if(data == "6"):
            break

menu()