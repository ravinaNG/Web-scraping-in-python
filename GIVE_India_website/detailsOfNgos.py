import requests
from bs4 import BeautifulSoup
import html5lib
from pprint import pprint
give_india_url = "https://www.giveindia.org/certified-indian-ngos"

def inviromentName(nameList):
    name = ""
    index = 0
    while(index < (len(nameList))):
        if(nameList[index] == "|"):
            break
        else:
            name = name + nameList[index]
            name = name + " "
        index = index + 1
    return name

def stateNames(nameList):
    name = ""
    index = 0
    while index<len(nameList):
        if(nameList[index]=="|"):
            num = index+1
            break
        index = index + 1
    while num < len(nameList):
        name = name + nameList[num]
        name = name + " "
        num = num + 1

    return name
def DetailsOfNgo(url):
    data = requests.get(give_india_url).text
    soup = BeautifulSoup(data, 'html5lib')
    ngos_class = soup.findAll('div', {'class':'nonprofit-card-container d-flex py-2 container'})
    detailsList = []
    for index in ngos_class:
        eachNgoDetails = {}
        allNgoData = index.find('div', {'class':'d-flex f-d-col col-10 col-sm-10'})
        ngoName = allNgoData.find('h5', {'class':'nonprofit-name mb-0'})
        ngo_name = ngoName.get_text() # Ngo Name
        # print (ngo_name)

        div = allNgoData.find('div')
        span = div.find('span')
        name_list = span.get_text()
        name_list = name_list.split()
        cause = inviromentName(name_list) # Couse name
        # print (cause)

        stateName = stateNames(name_list) # stateName
        # print (stateName)
        
        eachNgoDetails["NgoName"] = ngo_name
        eachNgoDetails["cause"] = cause
        eachNgoDetails["stateName"] = stateName

        detailsList.append(eachNgoDetails)
    return detailsList

details = DetailsOfNgo(give_india_url)
pprint (details)