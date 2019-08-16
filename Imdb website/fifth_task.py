from first_task import data_in_formate as moviesData
from fourth_task import urlList as url_list
import fourth_task
from pprint import pprint
import random
import time

def get_movie_list_details(ListOfUrl):
    wholeMoviesList = []
    user = 0
    length = len(ListOfUrl)
    for index in range(user, length):
        url = ListOfUrl[index-1]
        # print (index, end = " ")
        details = fourth_task.scrape_movie_details(url)
        # second = random.randint(1, 3)
        # pprint (details)
        # print (" ")
        # print ("************ Next ***********")
        # print (" ")
        # print (second)
        # time.sleep(second)
        wholeMoviesList.append(details)
    return wholeMoviesList

moviesDetailsList = get_movie_list_details(url_list)
# pprint (moviesDetailsList)


# task 6
# def analyse_movies_language(movieList):
#     languagesMovie = {}
#     for index in movieList:
#         languagesList = index['language']
#         for language in languagesList:
#             if(language not in languagesMovie):
#                 languagesMovie[language] = 1
#             else:
#                 languageMovies[language] = languagesMovie[language] + 1
#     return (languagesMovie)

# countMovie = analyse_movies_language(moviesDetailsList)
# pprint (countMovie)

# task 7
# def analyse_movies_director(movieList):
#     directorsMovie = {}
#     for index in movieList:
#         directorsList = index['director']
#         for director in directorsList:
#             if(director not in directorsMovie):
#                 directorsMovie[director] = 1
#             else:
#                 directorsMovie[director] = directorsMovie[director] + 1
#     return (directorsMovie)

# countMovie = analyse_movies_director(moviesDetailsList)
# pprint (countMovie)



# def getWholeLanguages(movieList):
#     languagesList = []
#     for movie in movieList:
#         langList = movie['language']
#         for language in langList:
#             if language not in languagesList:
#                 languagesList.append(language)
#     return languagesList

# languagesList = getWholeLanguages(moviesDetailsList)
# print (languagesList)


# def analyse_movies_language(movieList):
#     Hindi = 0
#     English = 0
#     Malayalam = 0
#     languages = {}
    
#     for movie in movieList[:10]:
#         if("Hindi" in movie['language']):
#             Hindi = Hindi + 1
#         if("English" in movie['language']):
#             English = English + 1
#         if("Malayalam" in movie['language']):
#             Malayalam = Malayalam + 1
    
#     languages['Hindi'] = Hindi
#     languages['English'] = English
#     languages['Malayalam'] = Malayalam
#     return languages

# languages = analyse_movies_language(moviesDetailsList)
# print (languages)
        
