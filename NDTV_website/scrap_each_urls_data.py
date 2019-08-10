import requests  
from bs4 import BeautifulSoup
import html5lib
from pprint import pprint
ndtv_url = "https://www.ndtv.com/latest?pfrom=home-mainnavgation"
data = requests.get(ndtv_url).text
soup = BeautifulSoup(data, 'html5lib')
ins_wid990 = soup.find('div', {'class':'ins_wid990'})
nstory_headers_classes = ins_wid990.findAll('div', {'class':'new_storylising_contentwrap'}) 
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
    ins_dateline = name_class.find('div', {'class':'ins_dateline'})
    # print (ins_dateline)

    try:
        a = ins_dateline.findAll('a')
        name = a[1].find('span', {'itemprop':'name'})
        print (name.get_text()) # Author
        print (" ")
    except:
        print ("In this articale there is no author.")
        print (" ")

    date = ins_dateline.find('span', itemprop="dateModified")
    print (date.text) # Date
    print (" ")

    ins_left_rhs = name_class.find('div', {'class':'ins_left_rhs'})
    articleBody = ins_left_rhs.find('div', {'itemprop':'articleBody'})
    print (articleBody.text) # Paragraph


urls = stor_urls(nstory_headers_classes)
url = "https://www.ndtv.com/india-news/sonia-rahul-gandhi-leave-meet-to-pick-new-congress-chief-priyanka-stays-back-2083263"
print (urls[5])
getDetailsOfArtical(urls[5])

