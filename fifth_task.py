from first_task import data_in_formate as moviesData
from fourth_task import urlList as url_list
import fourth_task
from pprint import pprint

print ("********* you will get 10 movies details if you select one movie ***************")

def storeMoviesName(movies_data):
    movie_names = []
    for index in movies_data:
        name = index['name']
        movie_names.append(name)
    return movie_names

movie_names = storeMoviesName(moviesData)
num = 1
for index in movie_names:
    print (num, end = " ")
    print (index)
    num = num + 1

user = int(input("Enter the number from which movie you want details:- "))
next_10 = user + 10
for index in range(user, next_10):
    url = url_list[index-1]
    print (index, end = " ")
    details = fourth_task.scrape_movie_details(url)
    pprint (details)
    print (" ")
    print ("************ Next ***********")
    print (" ")
