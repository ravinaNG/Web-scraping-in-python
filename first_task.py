import re
import requests
import json
import html5lib
from bs4 import BeautifulSoup
movie_link =  "https://www.imdb.com/india/top-rated-indian-movies/"
data = requests.get(movie_link)
movies_data = data.content
soup = BeautifulSoup(movies_data, 'html5lib')
# print(soup)
tbody = soup.find('tbody',{'class':'lister-list'})
# print (tbody)
for tr in tbody.findAll('tr'):
    td = (tr.find_all("td"))
    # print (td)
    i = 0
    while (i<len(td)):
        data = td[i].get_text()
        meta = re.sub(',', data)
        print (meta)
        i = i + 1
# just chacking










# print (tr.get_text())
# span = tbody.findAll('span')
# # for name in tr:
# #     print (name.get_text())
# # for year in span:
# #     print (year.get_text())
# rating = tbody.findAll('strong')
# # for rate in rating:
# #     print (rate.get_text())
# img = tbody.find('a')
# print (img.get)
# # for url in img:
#     print (url.get_text())