import requests  
from bs4 import BeautifulSoup
import html5lib
from pprint import pprint
import json
from os import path

ndtv_url = "https://www.ndtv.com/latest?pfrom=home-mainnavgation"
next_page = "https://www.ndtv.com/latest/page-"
next_page = next_page.split("-")

def openJsonFile(fileName, data):
    with open(fileName, 'w') as fileHandle:
        fileHandle.write(data)
        return fileHandle

def readJsonFile(fileName):
    with open(fileName, 'r') as fileHandle:
        data = fileHandle.read()
        return data

def getUrlData(url):
    data = requests.get(url).text
    soup = BeautifulSoup(data, 'html5lib')
    ins_wid990 = soup.find('div', {'class':'ins_wid990'})
    nstory_headers_classes = ins_wid990.findAll('div', {'class':'new_storylising_contentwrap'}) 
    return nstory_headers_classes

def stor_urls(data):
    urls_list = []
    num = 1
    for index in data:
        nstory_header = index.find('div', {'class':'nstory_header'})
        url = nstory_header.a['href']
        urls_list.append(url)
        num = num + 1
    return (urls_list)

def getDetailsOfArtical(url):
    dictionary = {}
    data = requests.get(url).text
    soup = BeautifulSoup(data, 'html5lib')
    title = soup.title.text # title
    # print (title)
    # print (" ")
    name_class = soup.find('div', {'class':'ins_lftcont640 clr', 'id':'newsDescriptionContainer'})
    try:   
        ins_dateline = name_class.find('div', {'class':'ins_dateline'})
        a = ins_dateline.findAll('a')
        name = a[1].find('span', {'itemprop':'name'})
        editedBy = name.get_text() # Author
        # print (editedBy)
        # print (" ")
        date = ins_dateline.find('span', itemprop="dateModified")
        newsDate = (date.text) # Date
        # print (newsDate)
        # print (" ")
        ins_left_rhs = name_class.find('div', {'class':'ins_left_rhs'})
        articleBody = ins_left_rhs.find('div', {'itemprop':'articleBody'})
        paragraph = articleBody.text # Paragraph
        # print (paragraph)

        dictionary['title'] = title
        dictionary['editedBy'] = editedBy
        dictionary['Date'] = newsDate
        dictionary['paragraph'] = paragraph
    except:
        dictionary['title'] = title
        pass
    return dictionary

index = 1
while(index <= 8):
    json_file = "page" + str(index) + ".json"
    wholePageDict = {}
    print (json_file)
    if (path.exists(json_file)):
        data = readJsonFile(json_file)
        print (data)
        index = index + 1
        continue
    else:
        page = str(-index)
        # print ("-=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--", end="  ")
        # print (index, end="  ")
        # print("--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-")
        # print (" ")
        next_page = next_page[0]+page
        nstory_headers_classes = getUrlData(next_page)
        urls = stor_urls(nstory_headers_classes)
        dictList = []
        url = 0
        while (url<len(urls)):
            # print (urls[url])
            detailsDict = getDetailsOfArtical(urls[url])
            dictList.append(detailsDict)
            # print (" ")
            url = url+1
        pageNo = "page"+str(index)
        wholePageDict[pageNo] = dictList
    newses = json.dumps(wholePageDict)
    pprint(newses)
    wholePagesData = openJsonFile(json_file, newses)
    print (wholePagesData)
    next_page = next_page.split("-")
    index = index + 1

# url = "https://gadgets.ndtv.com/wearables/sponsored/how-adidas-pulseboost-hd-will-revolutionize-urban-running-2075824"
# getDetailsOfArtical(url)