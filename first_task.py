import requests
from bs4 import BeautifulSoup
from pprint import pprint
import re
# import html5lib
movies_link = "https://www.imdb.com/india/top-rated-indian-movies/"
movies_data = requests.get(movies_link).content
soup = BeautifulSoup(movies_data, 'html')
# print (soup)
tbody = soup.find('tbody', {'class':'lister-list'})
# print (tbody)
trs = tbody.findAll('tr')
# print (type(trs)) # 'bs4.element.ResultSet' this is the type of trs but it is same like list.
# print (len(trs))
movies_data = []
td = 1
while (td <= len(trs)):
    dic = {}
    if(td == len(trs)):
        break
    name = trs[td].find('td', class_ = 'titleColumn').a.get_text()
    year = trs[td].find('td', class_ = 'titleColumn').span.get_text()
    demo = int(year.replace("(", "").replace(")", ""))
    # yea = list(year)
    # year = (yea.remove(yea[0]))
    # year = yea
    # yea = (year.remove(year[4]))
    # yea = year
    # year = ''.join(string for string in yea)
    # print(year)
    rating = trs[td].find('td', class_ = 'ratingColumn imdbRating').strong.get_text()
    url = trs[td].find('td', class_= 'posterColumn').a['href'] # her we don't use get_text() because the link is the value of a['href']
    movie_link = "https://www.imdb.com/" + url
    dic['name'] = name
    dic['year'] = demo
    dic['rating'] = rating
    dic['url'] = movie_link
    dic['position'] = td
    pprint (dic)
    td = td + 1
