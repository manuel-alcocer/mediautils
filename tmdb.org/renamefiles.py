#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from dbmods.create import mediaDBFile
from sys import argv, exit

def main():
    mediaDB = mediaDBFile()
    if mediaDB.status != 1:
        exit(1)

if __name__ == '__main__':
    main()
