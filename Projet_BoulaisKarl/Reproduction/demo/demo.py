#!/usr/bin/env python
#coding=utf-8

'''
Fonction utiliser pour la présentation:
-Génération d'adresse ip aléatoire
-Génération de nom d'ordinnateur aléatoire
'''


__author__ = 'Karl Boulais'

import random

class Demo():

    def randIP(self):
        ip = ".".join(map(str, (random.randint(0, 255) for _ in range(4))))
        return ip
    
    def randHostname(self):
        hostName = None
        return hostName

    def randMac(self):
        mac = None
        return mac


    def main(self):
        print(self.randIP())

if __name__ == "__main__":
    Demo().main()