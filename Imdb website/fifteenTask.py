from thirteenTask import movieDetailsWithCast
from fourth_task import urlList as moviesUrl
from os import path
from pprint import pprint
import json
from twelthTask import openJsonFile
from twelthTask import readJsonFile

def wholeMovieDetailswithCast(urList, movieScrape):
    moviesDetailsWithCast = []
    for url in urList:
        oneMovieDetails = movieDetailsWithCast(url)
        moviesDetailsWithCast.append(oneMovieDetails)
    return moviesDetailsWithCast

def analyse_actors(moviesDetails):
    actors = {}
    for movieDetails in moviesDetails:
        castList = movieDetails['cast']
        for imdb_id in castList:
            id = imdb_id['imdb_id']
            name = imdb_id['Name']
            if(id not in actors):
                actors[id]={}
                actors[id]["name"] = name
                actors[id]["num_movies"] = 1
            else:
                actors[id]['num_movies'] = actors[id]['num_movies'] + 1
    return actors

fileName = "analyse_actors.json"
if(path.exists(fileName)):
    print ("---===---===---===---===---===-- rading --===---===---===---===---===")
    data = readJsonFile(fileName)
    pprint (data)
else:
    print ("---===---===---===---===--- writing ---===---===---===---===---===---=")
    moviesDetails = wholeMovieDetailswithCast(moviesUrl, movieDetailsWithCast)
    actors = analyse_actors(moviesDetails)
    openJsonFile(fileName, actors)
    pprint (actors)