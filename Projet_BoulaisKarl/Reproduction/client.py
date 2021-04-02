#!/usr/bin/env python

import socket

def client():
    # [1]_ [2]_
    s = socket.socket()
    ip = socket.gethostname()
    host = ip
    port = 9999
    message = b'allo server!'

    s.connect((host, port))
    s.send(message)
    s.close

if __name__ == "__main__":
   client()


'''
.. rubric:: Notes de bas de page

.. [1]  https://www.tutorialspoint.com/python_network_programming/python_sockets_programming.htm 
        Principe de base d'une connexion TCP avec le module socket
.. [2]  https://gist.github.com/Integralist/3f004c3594bbf8431c15ed6db15809ae
        Utilisation de thread pour prendre en charge plusieurs connexions client à la fois
'''