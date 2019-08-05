from first_task import data_in_formate as moviesData
from bs4 import BeautifulSoup
# import html5lib
from pprint import pprint 
import requests

def storeMoviesUrl(movieData):
    urlList = []
    for index in movieData:
        urlList.append(index['url'])
    return urlList

def movieName(list):
    index = 0
    movie_name = ""
    while (index < len(list)):
        movie_name = movie_name + list[index]
        index = index + 1
    return movie_name

def languagesOfMovie(list):
    print (list)
    languages = []
    for index in list:
        language = index.get_text()
        languages.append(language)
    return language

def scrape_movie_details(movieUrl):
    list1 = []
    detailsss = {}
    getData = requests.get(movieUrl).content
    soup = BeautifulSoup(getData, 'html5lib')
    div = soup.find('div', {'class':'titleBar'})
    find_name = div.find('div', {'class':'title_wrapper'})
    name_year = find_name.h1.get_text()
    demo = name_year.split()
    remove_year = demo.pop()
    movie_name = (movieName(demo)) # movie name

    details = soup.find('div', {'class':'plot_summary'})
    director = details.a.get_text() 
    director_name = []
    director_name.append(director) # Derector name

    text = details.find('div', {'class':'summary_text'}).get_text()
    movie_text = text.strip() # movie text

    image_url = soup.find('div', {'class':'poster'})
    image_url = image_url.find('img')
    image_url = image_url.get('src') # poster image url

    country_class = soup.find('div', {'class':'article', 'id':'titleDetails'})
    txt_blocks = country_class.findAll('div', {'class':'txt-block'})
    for name in txt_blocks: 
        if 'Country' in name.text:
            country = name
        elif 'Language' in name.text:
            lang = name
    country_name = country.a.get_text() # country name
    lange = lang.findAll('a')
    # print (lange)
    # languages = []
    # language = lang.a.get_text() # language
    languages = languagesOfMovie(lange)
    print (languages)
    # languages.append(language)

    runTime = find_name.find('div', {'class':'subtext'}).time.get_text()
    runtime = runTime.strip() # Runtime

    genre = find_name.find('div', {'class':'subtext'}).a.get_text() # Genre
    genres = []
    genres.append(genre)

    # whole details in dictionary formate. :)
    detailsss['name'] = movie_name
    detailsss['director'] = director_name
    detailsss['country'] = country_name
    detailsss['language'] = languages
    detailsss['poster_image_url'] = image_url
    detailsss['bio'] = movie_text
    detailsss['runtime'] = runtime
    detailsss['genre'] = genres
    # pprint(detailsss)
    return detailsss

urlList = storeMoviesUrl(moviesData)
url = urlList[1]
# print (url)
movie_details = scrape_movie_details(url)
# pprint (movie_details)
