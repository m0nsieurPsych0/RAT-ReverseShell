#!/usr/#!/usr/bin/env python
#coding=utf-8

__author__ = 'Karl Boulais'

from argparse import ArgumentParser
import sys
import socket
import threading

from server import Server
from view import View
from dao import Dao, Columns

def argParse():
    p = ArgumentParser()
    group = p.add_mutually_exclusive_group()

    group.add_argument('-s','--server', dest='server', action='store_true', help='''

    Démarre le serveur et écoute pour des connexions. 
    Le mode est intérractif et permet de sélectionner des connexions pour démarrer une session Reverse Shell.

    ''')

    choiceList = ["ALL"]

    for choice in Columns:
        choiceList.append(str(choice))
    
    group.add_argument('-d', '--db', action='store', type=str, choices=choiceList, dest='db', help='''
    
    Entrez un ou plusieurs champ que vous voulez lister provenant de la base de donnée. 
    Un choix vide affiche tout le contenu de la base de donnée.    
    ''')
    
    return p

def error(text):
    print(f"\033[1;31;40m {text} \033[0;0m") 


def main():
    args = argParse().parse_args()
    
    if args.server:
        v = View()
        s = Server()
        s.main()
        v.interractiveMode(s)
    elif args.db:
        if args.db == "ALL":
            Dao().printAllClient()
        else:
            Dao().queryDB(args.db)
        


    # TODO :
    # - ARGPARSE:
    #           1- server et control
    #           2- query database
    
    
    
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