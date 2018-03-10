import socket
import sys
import webbrowser

def menu():
    HOST, PORT = "172.24.73.178", 9090
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    code = ""
    while(True):
        print("*************        MENU PRINCIPAL      *******************")
        data = input("1. Consultar el nombre del host del Servidor\n"
                    "2. Consultar la IP del Servidor\n"
                    "3. Consultar la cantidad de procesos ejecutandose en el servidor\n"
                    "4. Dar la hora en otro pais indicando el paıs\n"
                    "5. Poder enviar mensajes entre cliente y servidor\n"
                    "6. Salir\n"
                    "Opción: ")
        if (data == ""):
            menu()
        if (data == "6"):
            break
        if (data == "5"):
            print("¿servidor estas ahi?")
        if (data == '4'):
            opcion = input("1. Revisar Codigos paises\n"
                           "2. Escribir Codigo\n"
                           "Opción: ")
            if (opcion == ""):
                menu()
            elif (opcion == '1'):
                webbrowser.open('https://timezonedb.com/country-codes')
            code = input("Escribir Codigo: ")
        data = data + "," + code
        sock.sendto(data.encode(), (HOST, PORT))
        received = sock.recv(1024)
        print("************************************************************")
        print("Sent:     {}".format(data))
        print("Received: {}".format(received.decode()))
        print("************************************************************")

menu()