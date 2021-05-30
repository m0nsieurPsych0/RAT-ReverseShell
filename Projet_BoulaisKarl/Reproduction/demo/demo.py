#!/usr/bin/env python
#coding=utf-8

'''
Fonction utiliser pour la présentation:
-Génération d'adresse ip aléatoire
-Génération de nom d'ordinnateur aléatoire
'''


__author__ = 'Karl Boulais'

import random
from os import urandom, path
from enum import Enum

class Demo():

    def randomizer3000(self,maxsize):
        if random.randrange(0, 11) <= 5:
            andian = "little"
        else:
            andian = "big"
        return int.from_bytes(urandom(10), andian) % maxsize
    
    def randIP(self):
        ip = ".".join(map(str, (self.randomizer3000(255) for _ in range(4))))
        return ip
    
    def randHostname(self):
        names = []
        with open(f"{path.dirname(__file__)}/names.txt", 'r', encoding='UTF8') as f:
            names = f.readlines()

        hostName = names[self.randomizer3000(len(names))].strip()
        return hostName

    def randMac(self):
        mac = "-".join(map(hex, (self.randomizer3000(255) for _ in range(6))))
        return mac.replace('0x', '')

    def main(self):
        for _ in range(0, 100):
            print(self.randIP())
            print(self.randMac())
            print(self.randHostname())

class FakeData(Enum):
    # FIXME Produit des données fictives pour la démonstration
    HOSTNAME         = Demo().randHostname()
    LOCALIP          = Demo().randIP()
    PUBLICIP         = Demo().randIP()
    MAC              = Demo().randMac()

if __name__ == "__main__":
    Demo().main()