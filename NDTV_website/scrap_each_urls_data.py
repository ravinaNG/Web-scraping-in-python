import requests  
from bs4 import BeautifulSoup
import html5lib
from pprint import pprint
ndtv_url = "https://www.ndtv.com/latest?pfrom=home-mainnavgation"
next_page = "https://www.ndtv.com/latest/page-1"

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
        # print (ins_dateline)
    except:
        try:
            mainbody = soup.find('div', {'class':'mainbody'})
            modArticle = mainbody.find('div', {'class':'mod mod-article', 'id':'print-1'})
            ndRightDateTop = modArticle.find('div', {'class':'nd-right date-top'})
            contentWrap = ndRightDateTop.find('div', {'class':'content-wrap'})
            print (contentWrap.span.text) # Date
            print (" ")

            articleContent = modArticle.find('div', {'class':'article-content'})
            articleBody = articleContent.find('div', {'itemprop':'articleBody'})
            descfirst = articleBody.find('div', {'data-desc-first':'descfirst'})
            print (descfirst.text) # Paragraph

            descSecond = articleBody.find('div', {'data-desc-second':'descsecond'})
            ps = descSecond.findAll('p')
            for p in ps:
                print (p.text) # Paragraph
                print (" ")
        except:
            articleAuthor = soup.find('div', {'class':'article-author tpStl1'}) # date and Author
            b = articleAuthor.find('b')
            author = b.get_text()
            author = author.strip() # Author
            print (author)

            span = articleAuthor.find('span')
            print (span.text)

            article_storybody = soup.find('div', {'class':'article_storybody'})
            paragraph = article_storybody.get_text()
            paragraph = paragraph.strip()
            print (paragraph)
    try:
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


nstory_headers_classes = getUrlData(ndtv_url)
urls = stor_urls(nstory_headers_classes)
# url = "https://doctor.ndtv.com/living-healthy/9-healthy-drinks-other-than-water-to-include-in-your-diet-2083565"
# getDetailsOfArtical(url)
url = 0
while (url<len(urls)):
    print (urls[url])
    getDetailsOfArtical(urls[url])
    print (" ")
    url = url+1
