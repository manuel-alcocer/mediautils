#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from os import getcwd, path
from sqlite3 import connect

class mediaDBFile:
    def __init__(self):
        self.dbFile = '.mediainfo.db'
        self.currentDir = getcwd()
        self.absDBFile = path.join(self.currentDir,self.dbFile)
        self.status = 0
        self.checkDB()

    def checkDB(self):
        if not path.isfile(self.absDBFile):
            self.createDBFile()

    def createDBFile(self):
        try:
            conn = connect(self.absDBFile)
            c = conn.cursor()
            c.execute('''CREATE TABLE media (
            id       INTEGER PRIMARY KEY AUTOINCREMENT,
            name     TEXT,
            synopsis TEXT,
            thumb    BLOB)''')
            conn.commit()
            conn.close()
        except:
            self.status = 1

def main():
    media = mediaDBFile()

if __name__ == '__main__':
    main()
