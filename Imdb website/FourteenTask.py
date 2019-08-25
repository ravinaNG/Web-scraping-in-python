from fifteenTask import wholeMovieDetailswithCast
from fourth_task import urlList 
from thirteenTask import movieDetailsWithCast
from pprint import pprint

def analyse_co_actors(updatedMoviesDetails):
    coALeadActors = {}
    for movieD in updatedMoviesDetails:
        listOfCast = movieD['cast']
        leadActorId = listOfCast[0]['imdb_id']
        # print (leadActorId)
        leadActorName = listOfCast[0]['Name']
        # print (leadActorName)
        for movieD2 in updatedMoviesDetails:
            listOfCast2 = movieD2['cast']
            coActorId = listOfCast2[1]['imdb_id']
            coActorName = listOfCast2[1]['Name']
            if(leadActorId == listOfCast2[0]['imdb_id']):
                if (leadActorId not in coALeadActors):
                    coALeadActors[leadActorId] = {}
                    coALeadActors[leadActorId]['Name'] = leadActorName
                    coALeadActors[leadActorId]['frequent_co_actors'] = []
                    coActorDic = {}
                    coActorDic['Name'] = coActorName
                    coActorDic['imdb_id'] = coActorId
                    coActorDic['num_movie'] = 1
                    coALeadActors[leadActorId]['frequent_co_actors'].append(coActorDic)
                else:
                    coActorsList = coALeadActors[leadActorId]['frequent_co_actors']
                    num = 1
                    length = len(coActorsList)
                    for frequent_co_actors in coActorsList:
                        num = num + 1
                        if(frequent_co_actors['imdb_id'] == coActorId):
                            frequent_co_actors['num_movie'] = frequent_co_actors['num_movie'] + 1
                            coALeadActors[leadActorId]['frequent_co_actors'] = coActorsList
                            break
                        if(num+1 == length):                
                            coActorDic = {}
                            coActorDic['Name'] = coActorName
                            coActorDic['imdb_id'] = coActorId
                            coActorDic['num_movie'] = 1
                            coActorsList.append(coActorDic)
                            coALeadActors[leadActorId]['frequent_co_actors'] = coActorsList
    return coALeadActors


updatedMoviesDetails = wholeMovieDetailswithCast(urlList, movieDetailsWithCast)
coActorsOfLeadActors = analyse_co_actors(updatedMoviesDetails)
# pprint (coActorsOfleadActors)
CoAndLeadActors = {}
for id, CoALeadActor in coActorsOfLeadActors.items():
    for coAList, numMovie in CoALeadActor.items():
        if(CoALeadActor['frequent_co_actors'][0]['num_movie'] != 1):
            # print (CoALeadActor['frequent_co_actors'][0]['num_movie'])
            CoAndLeadActors[id] = CoALeadActor
pprint (CoAndLeadActors)