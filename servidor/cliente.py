import socket
import sys
import webbrowser

HOST, PORT = "172.24.93.7", 8090
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def enviar(data, code):
    global sock, HOST, PORT
    data = data + "," + code
    sock.sendto(data.encode(), (HOST, PORT))
    received = sock.recv(1024)
    print("************************************************************")
    print("Sent:     {}".format(data))
    print("Received: {}".format(received.decode()))
    print("************************************************************")

def subMenu(data):
    code = ""
    option = input("\na. enviar mensaje al chat\nb. salir de chat\nopcion: ")
    if option == "a":
        print("a")
        code = input("escriba el mensaje: ")
        data = "9"
        enviar(data, code)
        subMenu(data)
    elif option == "b":
        print("b")
        data = "8"
        enviar(data, code)
        menu()
    subMenu(data)

def menu():
    global sock, HOST, PORT
    code = ""
    sock.connect((HOST, PORT))
    while(True):
        print("*************        MENU PRINCIPAL      *******************")
        data = input("1. Consultar el nombre del host del Servidor\n"
                    "2. Consultar la IP del Servidor\n"
                    "3. Consultar la cantidad de procesos ejecutandose en el servidor\n"
                    "4. Dar la hora en otro pais indicando el paıs\n"
                    "5. Poder enviar mensajes entre cliente y servidor\n"
                    "6. Unirse a chat\n"
                    "7. Salir\n"
                    "Opción: ")
        if (data == ""):
            menu()
        if (data == "6"):
            enviar(data,code)
            subMenu(data)
        if (data == "7"):
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
        enviar(data, code)

menu()