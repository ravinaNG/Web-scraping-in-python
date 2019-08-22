from fifteenTask import wholeMovieDetailswithCast
from fourth_task import urlList 
from thirteenTask import movieDetailsWithCast
from pprint import pprint

def analyse_co_actors(updatedMoviesDetails):
    coActors = {}
    for movieDetails in updatedMoviesDetails:
        print ('Ravina')
        cast = movieDetails['cast']
        for actor in cast[:5]:
            print ('Ravina')
            id = actor['imdb_id']
            name = actor['Name']
            for movie in updatedMoviesDetails:
                print ('Ravina')
                castList = movie['cast']
                cast = 0
                while (cast < len(castList)):
                # for cast in castList:
                    if (id == castList[cast]['imdb_id']):
                        if (id not in coActors):
                            coActors[id] = {}
                            coActors[id]["Name"] = name
                            coActors[id]['frequent_co_actors'] = []
                            coDirector = {}
                            if(cast+1 == len(castList)):
                                coCast = castList[0]
                            else:
                                coCast = castList[cast+1]
                            coDirector['num_movie'] = 1
                            coDirector['imdb_id'] = coCast['imdb_id']
                            coDirector['Name'] = coCast['Name']
                            # coDirector['num_movie'] = coDirector['num_movie'] + 1
                            coActors[id]['frequent_co_actors'].append(coDirector)
                        if (id in coActors):
                            if(cast+1 == len(castList)):
                                coCast = castList[0]
                                coId = coCast['imdb_id']
                            else:
                                coCast = castList[cast+1]
                                coId = coCast['imdb_id']
                            for frequent_co_actor in coActors[id]['frequent_co_actors']:
                                if(frequent_co_actor['imdb_id'] == coId):
                                    frequent_co_actor['num_movie'] = frequent_co_actor['num_movie'] + 1
                            else:
                                coDirector = {}
                                coDirector['imdb_id'] = coCast['imdb_id']
                                coDirector['Name'] = coCast['Name']
                                coDirector['num_movie'] = 1
                                coActors[id]['frequent_co_actors'].append(coDirector)
    return coActors
updatedMoviesDetails = wholeMovieDetailswithCast(urlList, movieDetailsWithCast)
coActorsOfleadActors = analyse_co_actors(updatedMoviesDetails)
pprint (coActorsOfleadActors)