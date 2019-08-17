from fifth_task import moviesDetailsList as moviesDetails
from pprint import pprint

def analyse_language_and_directors(moviesList):
    directorsLanguage = {}
    for movie in moviesList:
        directorList = movie['director']
        for director in directorList:
            if director not in directorsLanguage:
                directorsLanguage[director] = {}
                for movieD in moviesList:
                    languageList = movieD['language']
                    directorList2 = movieD['director']
                    for language in languageList:
                        if director in directorList2:
                            if language not in directorsLanguage[director]:
                                directorsLanguage[director][language] = 1
                            else:
                                directorsLanguage[director][language] = directorsLanguage[director][language] + 1
    return directorsLanguage       

languagesOfDirectors = analyse_language_and_directors(moviesDetails)
pprint (languagesOfDirectors)