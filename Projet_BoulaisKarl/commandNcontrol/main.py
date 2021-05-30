#!/usr/#!/usr/bin/env python
#coding=utf-8

__author__ = 'Karl Boulais'

from argparse import ArgumentParser
import sys
import socket
import threading

from server import Server
from view import View

def argParse():
    p = ArgumentParser()

    return p


def main():
    v = View()
    s = Server()
    s.main()
 
    v.interractiveMode(s)
    


if __name__ == "__main__":
   main()



'''
.. rubric:: Notes de bas de page

.. [1]  https://www.g-loaded.eu/2016/11/24/how-to-terminate-running-python-threads-using-signals/ 
        Méthode pour terminer les autres thread (grâcieusement) qui sont dans une boucle infinie
        On utilise un signal à partir du main thread pour envoyer une exception qui change un flag dans les
        Thread à arrêter

.. [2]  https://stackoverflow.com/questions/18018033/how-to-stop-a-looping-thread-in-python 
        Méthode pour terminer les autres thread (grâcieusement) qui sont dans une boucle infinie
        On utilise un attribut qu'on modifie lorqu'on veut arrêter un thread

'''