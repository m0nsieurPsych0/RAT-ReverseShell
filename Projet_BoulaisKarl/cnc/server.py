#!/usr/bin/env python

__author__ = "Karl Boulais"


import socket
import threading

# Attention au nombre de thread

def server() -> str:
    # [1]_ [2]_  

    s = socket.socket()

    host = socket.gethostname()
    port = 9999
    s.bind((host, port))

    s.listen(5)

    while True:
        c, addr = s.accept()
        #FIXME: En prod on n'imprime plus TODO: sinon que dans un fichier log
        print('Got connection from', addr)

        #TODO: recevoir les infos clients et les ajouters à la base de donnée
        print(str(c.recv(1024)))
        c.close()



if __name__ == "__main__":
   server()


'''
.. rubric:: Notes de bas de page

.. [1]  https://www.tutorialspoint.com/python_network_programming/python_sockets_programming.htm 
        Principe de base d'une connexion TCP avec le module socket
.. [2]  https://gist.github.com/Integralist/3f004c3594bbf8431c15ed6db15809ae
        Utilisation de thread pour prendre en charge plusieurs connexions client à la fois
'''