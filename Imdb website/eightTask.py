from fourth_task import urlList as url_list
import fourth_task
import requests
from bs4 import BeautifulSoup
from os import path
import json
from pprint import pprint

url = url_list[0]
idList = url.split('/')
fileName = idList[4]+".json"
print (fileName)

def openJsonFile(fileName, Data):
    data = json.dumps(Data)
    with open (fileName, 'w') as write_it:
        write_it.write(data)
    return write_it

def readJsonFile(fileName):
    with open(fileName, 'r') as read_it:
        data = read_it.read()
    return data

if (path.exists(fileName)):
    movieData = readJsonFile(fileName)
    print ("-=--=--=--=--=--=--=--=--=-- Reading file --=--=--=--=--=--=--=--=-")
    print (" ")
    pprint (movieData)
else:
    movieDetails = fourth_task.scrape_movie_details(url)
    openJsonFile(fileName, movieDetails)
    print ("-=--=--=--=--=--=--=--=--=--=--=-- writing --=--=--=---=---=--=--=--")
    print (" ")
    pprint (movieDetails)