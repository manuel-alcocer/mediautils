#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from requests import get
from os import environ

tmdbBaseURL = 'https://api.themoviedb.org'
tmdbAPIVersion = '3'

class tmdb:
    def __init__(self):
        self.tmdbAPIKey = environ['TMDBAPIv3']
        
    def search(self, mediatype, query, page='1'):
        payload = {
                    'api_key' : self.tmdbAPIKey,
                    'language' : 'es-ES',
                    'query' : query,
                    'page' : page
                    }
        urlPath = '%s/%s/%s/%s' %(tmdbBaseURL, tmdbAPIVersion, 'search', mediatype)
        self.response = get(urlPath, params = payload)
        self.responseDict = self.response.json()
    
    def getTVInfo(self, args):
        idnum, season, episode = args
        payload = {
                    'api_key' : self.tmdbAPIKey,
                    'language' : 'es-ES',
                    }
        urlPath = '%s/%s/tv/%s/season/%s/episode/%s' %(tmdbBaseURL, tmdbAPIVersion, idnum, season, episode)
        self.response = get(urlPath, params = payload)
        self.responseDict = self.response.json()
