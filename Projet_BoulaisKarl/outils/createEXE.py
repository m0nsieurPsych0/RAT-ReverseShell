#!/usr/bin/env python
#coding=utf-8
__author__ = 'Karl Boulais'

import subprocess

class CreateEXE():

    def __init__(self):
        pass

    ## Compiler en utilisant pyinstaller ##

    def createEXE(self,path):
        # Créer un programme qui contient toutes les dépendances python en un seul fichier
        subprocess.call(f"pyinstaller.exe --clean --onefile {path}")

    def main(self):
        pass

if __name__ == "__main__":
    CreateEXE().main()