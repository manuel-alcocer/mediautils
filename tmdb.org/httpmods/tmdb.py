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
        if len(args) == 1:
            urlPath = 'tv/%s' % args
            self.requestType = 'tvshow'
        elif len(args) == 2:
            urlPath = 'tv/%s/season/%s' % args
            self.requestType = 'tvseason'
        else:
            urlPath = 'tv/%s/season/%s/episode/%s' % args
            self.requestType = 'tvepisode'
        payload = {
                    'api_key' : self.tmdbAPIKey,
                    'language' : 'es-ES',
                    }
        urlPath = '%s/%s/%s' %(tmdbBaseURL, tmdbAPIVersion, urlPath)
        self.response = get(urlPath, params = payload)
        self.responseDict = self.response.json()
