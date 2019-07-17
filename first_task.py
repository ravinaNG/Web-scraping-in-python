import requests
import json
import html5lib
from pprint import pprint
from bs4 import BeautifulSoup
movie_link =  "https://www.imdb.com/india/top-rated-indian-movies/"
data = requests.get(movie_link)
movies_data = data.content
soup = BeautifulSoup(movies_data, 'html5lib')
tbody = soup.find('tbody',{'class':'lister-list'})
trs = tbody.find_all('tr')
def scrape_top_list():
    dic_list = []
    i = 0
    for tr in trs: 
        dic = {}
        i = i + 1
        name = tr.find('td', class_= 'titleColumn').a.get_text()
        year = tr.find('td', class_= 'titleColumn').span.get_text()
        url_movies = tr.find('td', class_='titleColumn').a['href']
        link =  'https://www.imdb.com' + url_movies
        rate = tr.find('td', class_= 'ratingColumn imdbRating').strong.get_text()
        dic['year']= int(year[1:5])
        dic['rating'] = float(rate)
        dic['POSTION'] = int(i)
        dic['name'] = str(name)
        dic['url']= str(link)
        # print (dic)
        dic_list.append(dic)
    return dic_list
top_movies = (scrape_top_list()) 
pprint (top_movies)































# span = tbody.findAll('span')
# tr = tbody.find_all('tr')
# rating = tbody.findAll('strong')
# img = tbody.findAll('a')
# for url in img:
#     print (url.get_text()) # Names of movies
# for name in tr:
#     print (name.get_text())  # in tr everything is there like name, year, rating, position.
# for year in span:
#     print (year.get_text())  # year of the movies 
# for rate in rating:
#     print (rate.get_text()) # rating of movies