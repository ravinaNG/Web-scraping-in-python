import requests
from bs4 import BeautifulSoup
from pprint import pprint


# import html5lib
movies_link = "https://www.imdb.com/india/top-rated-indian-movies/"
movies_data = requests.get(movies_link).text


# print (type(movies_data))
soup = BeautifulSoup(movies_data, 'html5lib')
tbody = soup.find('tbody', {'class':'lister-list'})
trs = tbody.findAll('tr')


# # print (type(trs)) # 'bs4.element.ResultSet' this is the type of trs but it is same like list.
def scrap_top_list(trs):
    movies_data = []
    td = 0
    while (td < len(trs)):
        dic = {}
        name = trs[td].find('td', class_ = 'titleColumn').a.get_text()
        year = trs[td].find('td', class_ = 'titleColumn').span.get_text()
        movie_rlg_year = int(year.replace("(", "").replace(")", ""))
        # year = ''.join(string for string in yea)
        rating = trs[td].find('td', class_ = 'ratingColumn imdbRating').strong.get_text()
        url = trs[td].find('td', class_= 'titleColumn').a['href'] # her we don't use get_text() because the link is the value of a['href']
        movie_link = "https://www.imdb.com" + url
        dic['name'] = name
        dic['year'] = movie_rlg_year
        dic['rating'] = rating
        dic['url'] = movie_link
        dic['position'] = td+1
        movies_data.append(dic) 
        td = td + 1
    return movies_data

data_in_formate = (scrap_top_list(trs))
# pprint (data_in_formate)
