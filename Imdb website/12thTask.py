from fourth_task import urlList as moviesUrl
import requests
from bs4 import BeautifulSoup
from pprint import pprint
import json
import os

def openJsonFile(fileName, data):
    jsonData = json.dumps(data)
    with open(fileName, 'w') as writer:
        writer.write(jsonData)

def readJsonFile(fileName):
    with open(fileName, 'r') as reader:
        jsonData = reader.read()
    data = json.loads(jsonData)
    return data

def scrape_movie_cast(url):
    res = requests.get(url).content
    soup = BeautifulSoup(res, 'html5lib')
    subnav = soup.find('div', {'id':'quicklinksBar', 'class':'subnav'})
    div = subnav.find('div', {'id':'quicklinksMainSection'})
    castUrl = div.a['href']

    # cast url
    add = "https://www.imdb.com"
    castUrl = add + castUrl + "?ref_=tt_ql_1" 
    res = requests.get(castUrl).content
    soup = BeautifulSoup(res, 'html5lib')
    header = soup.find('div', {'id':'fullcredits_content', 'class':'header'})
    cast_list = header.find('table', {'class':'cast_list'})
    tbody = cast_list.find('tbody')
    oddTrs = tbody.findAll('tr', {'class':'odd'})
    evenTrs = tbody.findAll('tr', {'class':'even'})

    listOfIdsAndCast = []
#     print ("********************* odd ******************************")
    for oddTr in oddTrs:
        dictOfCastAndId = {}
        td = oddTr.findAll('td')
        castLink = td[1].a['href']
        split = castLink.split('/')
        cast_id = split[2]
        name = td[1].a.get_text()
        name = name.strip()
        dictOfCastAndId["imdb_id"] = cast_id
        dictOfCastAndId['Name'] = name
        listOfIdsAndCast.append(dictOfCastAndId)
#     print("*********************** even ******************************")
    for evenTr in evenTrs:
        dictOfCastAndId = {} 
        td = evenTr.findAll('td') 
        castLink = td[1].a['href']
        split = castLink.split('/')
        cast_id = split[2]
        name = td[1].a.get_text()
        dictOfCastAndId["imdb_id"] = cast_id
        dictOfCastAndId['Name'] = name
        listOfIdsAndCast.append(dictOfCastAndId)
    return listOfIdsAndCast

#     print (oddTrs)
movieUrl = moviesUrl[0]
castAndId = scrape_movie_cast(movieUrl)
pprint (castAndId)
