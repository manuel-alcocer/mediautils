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
    m = tmdb()
    m.getTVInfo(tuple(optionsDict['args']))
    if m.response.status_code == 200:
        if m.requestType == 'tvshow':
            showTVInfo(m.responseDict)
        elif m.requestType == 'tvseason':
            showSeasonInfo(m.responseDict)
        else:
            showEpisodeInfo(m.responseDict)

def showTVInfo(responseDict):
    print ('Nombre: %s' % responseDict['name'])
    print ('Temporadas: %s' % responseDict['number_of_seasons'])
    print ('Episodios: %s' % responseDict['number_of_episodes'])

def showSeasonInfo(responseDict):
    print ('Temporada: %d' % responseDict['season_number'])
    print ('Episodios: %d\n' % len(responseDict['episodes']))
    for episode in responseDict['episodes']:
        print ('Número: %d' % episode['episode_number'])
        print ('Título: %s' %episode['name'].strip())
        print ('Descripción: %s\n' %episode['overview'].strip())

def showEpisodeInfo(responseDict):
    print ('Título: %s' % responseDict['name'].strip())
    print ('Descripción: %s' % responseDict['overview'].strip())

def makeSearch(optionsDict):
    m = tmdb()
    if 'p' in optionsDict.keys():
        pNum = optionsDict['p']
    else:
        pNum = 1
    if 'r' in optionsDict.keys():
        rNum = int(optionsDict['r']) - 1
    else:
        rNum = 0
    m.search(optionsDict['t'], optionsDict['args'][0], str(pNum))
    printResults(m, rNum)

def printResults(m, rNum):
    print ('Páginas: %d' % m.responseDict['total_pages'])
    print ('Resultados: %d' % m.responseDict['total_results'])
    if 0 < len(m.responseDict['results']) and rNum + 1 <= len(m.responseDict['results']):
        idNum = m.responseDict['results'][rNum]['id']
        name = m.responseDict['results'][rNum]['name']
        overview = m.responseDict['results'][rNum]['overview']
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
