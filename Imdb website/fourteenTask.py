from fifteenTask import wholeMovieDetailswithCast
from fourth_task import urlList 
from thirteenTask import movieDetailsWithCast
from pprint import pprint

def analyse_co_actors(updatedMoviesDetails):
    coActors = {}
    num = 0
    for movieDetails in updatedMoviesDetails:
        cast = movieDetails['cast']
        for actor in cast[:5]:
            id = actor['imdb_id']
            name = actor['Name']
            for movie in updatedMoviesDetails:
                castList = movie['cast']
                for cast in castList:
                    if (id == cast['imdb_id']):
                        if (id not in coActors):
                            num = 1
                            coActors[id] = {}
                            coActors[id]["Name"] = name
                            coActors[id]['frequent_co_actors'] = []
                            directorDic = {}
                            directorDic['num_movie'] = 1
                        elif(num == 1):
                            num = 0
                            directorDic['imdb_id'] = cast['imdb_id']
                            directorDic['Name'] = cast['Name']
                            directorDic['num_movie'] = directorDic['num_movie'] + 1
                            coActors[id]['frequent_co_actors'].append(directorDic)
    return coActors
updatedMoviesDetails = wholeMovieDetailswithCast(urlList, movieDetailsWithCast)
coActorsOfleadActors = analyse_co_actors(updatedMoviesDetails)
pprint (coActorsOfleadActors)