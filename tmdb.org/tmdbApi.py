#!/usr/bin/env python3
# -*- coding: utf-8-*-

# Ejemplos de uso:
#   ./tmdbApi -t tv -c search simpson
#   ./tmdbApi -t tv -c search -p 2 -r2 cop 

from sys import argv, exit
from getopt import getopt, GetoptError

from httpmods.tmdb import tmdb

def usage():
    print ('''
Uso del script:
    -c [search,info]
    -t [tv,episode,movie] :
        [ -p page_number ]
        [ -r result_number ]
    -i id
    ''')

def runCommand(optionsDict):
    if optionsDict['c'] == 'search':
        makeSearch(optionsDict)
    if optionsDict['c'] == 'info':
        if optionsDict['t'] == 'tv':
            getTVInfo(optionsDict)

def getTVInfo(optionsDict):
    mediaTest = tmdb()
    mediaTest.getTVInfo(optionsDict['args'])
    print (mediaTest.responseDict)

def makeSearch(optionsDict):
    mediaTest = tmdb()
    if 'p' in optionsDict.keys():
        pNum = optionsDict['p']
    else:
        pNum = 1
    if 'r' in optionsDict.keys():
        rNum = int(optionsDict['r']) - 1
    else:
        rNum = 0
    mediaTest.search(optionsDict['t'], optionsDict['args'][0], str(pNum))
    printResults(mediaTest, rNum)

def printResults(mediaTest, rNum):
    print ('Páginas: %d' % mediaTest.responseDict['total_pages'])
    print ('Resultados: %d' % mediaTest.responseDict['total_results'])
    if 0 < len(mediaTest.responseDict['results']) and rNum + 1 <= len(mediaTest.responseDict['results']):
        idNum = mediaTest.responseDict['results'][rNum]['id']
        name = mediaTest.responseDict['results'][rNum]['name']
        overview = mediaTest.responseDict['results'][rNum]['overview']
        print ('id: %s' %idNum)
        print ('Nombre: %s' %name)
        print ('Descripción: %s' %overview )
    else:
        print ('Página o resultado fuera de rango')
        
def main():
    try:
        optionlist, args = getopt(argv[1::],'c:t:p:r:')
    except GetoptError as err:
        print (err)
        usage()
        exit(2)
    optionsDict = {}
    for o,a in optionlist:
        optionsDict[o.strip('-')] = a
    optionsDict['args'] = args
    runCommand(optionsDict)
    
if __name__ == '__main__':
    main()
