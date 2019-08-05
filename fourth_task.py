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

def languagesOfMovie(length, list):
    languages = []
    for index in range(1, length):
        if(list[index] == '|'):
            pype = list[index]
            list.remove(pype)
        languages.append(list[index])
    return languages

def scrape_movie_details(movieUrl):
    list1 = []
    details = {}
    lang = []
    getData = requests.get(movieUrl).content
    soup = BeautifulSoup(getData, 'html5lib')
    div = soup.find('div', {'class':'titleBar'})
    find_name = div.find('div', {'class':'title_wrapper'})
    name_year = find_name.h1.get_text()
    demo = name_year.split()
    remove_year = demo.pop()
    movie_name = (movieName(demo)) # movie name

    plot_summary = soup.find('div', {'class':'plot_summary'})
    credit_summary_item = plot_summary.find('div', {'class':'credit_summary_item'})
    key_value = credit_summary_item.text
    key_value = key_value.strip()
    directors = key_value.split()
    length = len(directors)
    directors_name = languagesOfMovie(length, directors) # Derectors name
    # print (directors_name)
    # director = details.a.get_text() 
    # director_name = []
    # director_name.append(director) # Derector name

    text = plot_summary.find('div', {'class':'summary_text'}).get_text()
    movie_text = text.strip() # movie text

    image_url = soup.find('div', {'class':'poster'})
    image_url = image_url.find('img')
    image_url = image_url.get('src') # poster image url

    country_class = soup.find('div', {'class':'article', 'id':'titleDetails'})
    txt_blocks = country_class.findAll('div', {'class':'txt-block'})
    for name in txt_blocks: 
        if 'Country' in name.text:
            country = name.text 
            country = country.strip()
            key_value = country.split()
            country_name = key_value[1] # country

        elif 'Language' in name.text:
            lang = name.text
            lang = lang.strip()
            languages = lang.split()
            length = len(languages)-1

    languages = languagesOfMovie(length, languages) # language
    # print (languages)

    runTime = find_name.find('div', {'class':'subtext'}).time.get_text()
    runtime = runTime.strip() # Runtime

    genre = find_name.find('div', {'class':'subtext'}).a.get_text() # Genre
    genres = []
    genres.append(genre)

    # whole details in dictionary formate. :)
    details['name'] = movie_name
    details['director'] = directors_name
    details['country'] = country_name
    details['language'] = languages
    details['poster_image_url'] = image_url
    details['bio'] = movie_text
    details['runtime'] = runtime
    details['genre'] = genres
    return details

urlList = storeMoviesUrl(moviesData)
url = urlList[5]
movie_details = scrape_movie_details(url)
pprint (movie_details)
