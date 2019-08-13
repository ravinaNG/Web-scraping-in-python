import requests  
from bs4 import BeautifulSoup
import html5lib
from pprint import pprint
ndtv_url = "https://www.ndtv.com/latest?pfrom=home-mainnavgation"
next_page = "https://www.ndtv.com/latest/page-6"

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
    data = requests.get(url).text
    soup = BeautifulSoup(data, 'html5lib')
    print(soup.title.text)
    print (" ")
    name_class = soup.find('div', {'class':'ins_lftcont640 clr', 'id':'newsDescriptionContainer'})
    try:   
        ins_dateline = name_class.find('div', {'class':'ins_dateline'})
        a = ins_dateline.findAll('a')
        name = a[1].find('span', {'itemprop':'name'})
        print (name.get_text()) # Author
        print (" ")
        date = ins_dateline.find('span', itemprop="dateModified")
        print (date.text) # Date
        print (" ")
        ins_left_rhs = name_class.find('div', {'class':'ins_left_rhs'})
        articleBody = ins_left_rhs.find('div', {'itemprop':'articleBody'})
        print (articleBody.text) # Paragraph
    except:
        pass

nstory_headers_classes = getUrlData(next_page)
urls = stor_urls(nstory_headers_classes)
url = 0
print (len(urls))
while (url<len(urls)):
    print (urls[url])
    getDetailsOfArtical(urls[url])
    print (" ")
    url = url+1

# url = "https://gadgets.ndtv.com/wearables/sponsored/how-adidas-pulseboost-hd-will-revolutionize-urban-running-2075824"
# getDetailsOfArtical(url)