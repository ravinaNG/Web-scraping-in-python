import requests
from bs4 import BeautifulSoup
from pprint import pprint

url = "https://paytmmall.com/fmcg-sauces-pickles-glpid-101471?page=1&latitude=12.868065800000002&longitude=77.7128736"

def topDetailsOfPickles(url):
    data = requests.get(url).content
    soup = BeautifulSoup(data, 'html5lib')
    _2mYo = soup.find('div', {'class':'_2mYo'})
    _3RA = _2mYo.find('div', {'class':'_3RA-'})
    _1fje = _3RA.findAll('div', {'class':'_1fje'})

    AlldetailsList = []
    for index in _1fje:
        OnedetailsDict = {}
        _2i1r = index.find('div', {'class':'_2i1r'})
        _3WhJ = _2i1r.find('div', {'class':'_3WhJ'})

        url = _3WhJ.a['href'] # url

        name = _3RA.a['title'] # name

        _3nWP = _3WhJ.find('div', {'class':'_3nWP'})
        imageUrl = _3nWP.img['src'] # image url

        _2bo3 = _3WhJ.find('div', {'class':'_2bo3'})
        _1kMS = _2bo3.find('div', {'class':'_1kMS'})
        prise = _1kMS.span.text # prise

        OnedetailsDict["pickleUrl"] = url
        OnedetailsDict["Name"] = name
        OnedetailsDict["ImageUrl"] = imageUrl
        OnedetailsDict["peise"] = prise

        AlldetailsList.append(OnedetailsDict)
    return AlldetailsList

topDetails = topDetailsOfPickles(url)
pprint (topDetails)