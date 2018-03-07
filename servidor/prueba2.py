import socket
import sys
import webbrowser


def menu():
    print("*************        MENU PRINCIPAL      *******************")
    HOST, PORT = "172.24.43.158", 8090
    data = input("1. Consultar el nombre del host del Servidor\n"
                 "2. Consultar la IP del Servidor\n"
                 "3. Consultar la cantidad de procesos ejecutandose en el servidor\n"
                 "4. Dar la hora en otro pais indicando el paıs\n"
                 "5. Poder enviar mensajes entre cliente y servidor\n"
                 "Opción: ")

    if(data == '4'):
        opcion = input("1. Revisar Codigos paises\n"
                     "2. Escribir Codigo\n"
                     "Opción: ")
        if(opcion == '1'):
            webbrowser.open('https://timezonedb.com/country-codes')

        data = input("Escribir Codigo: ")

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    sock.sendto(data.encode(), (HOST, PORT))
    received = sock.recv(1024)

    print("************************************************************")
    print("Sent:     {}".format(data))
    print("Received: {}".format(received.decode()))
    print("************************************************************")

    menu()

menu()