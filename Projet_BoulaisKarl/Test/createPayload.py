#!/usr/bin/env python
#coding=utf-8
__author__ = 'Karl Boulais'

import base64
from sys import argv

class createPayload():
   
    def createPayload(self, programName):
        # importer un fichier en tant que byte array
        with open(programName, "rb") as program:
         b64 = base64.b64encode(program.read())

        # Écrire le byte array dans un fichier texte
        with open(f"{programName}byte.txt", mode="w") as copy:
            copy.write(str(b64))

    def main(self):
        self.createPayload(argv[1])

if __name__ == "__main__":
    createPayload().main()