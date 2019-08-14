from first_task import data_in_formate as moviesData
from bs4 import BeautifulSoup
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

def languagesOfMovie(index, length, split_list):
    languages = []
    if('UA' in split_list):
        length = len(split_list)-5
        index = 5
    if('U' in split_list):
        length = len(split_list)-5
        index = 5
    if('A' in split_list):
        length = len(split_list)-5
        index = 5
    if('Unrated' in split_list):
        length = len(split_list)-5
        index = 5
    while(index<length):
        if(split_list[index] == '|'):
            pype = split_list[index]
            split_list.remove(pype)
            index = index -1
            length = len(split_list)
        else:
            languages.append(split_list[index])
        index = index + 1
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
    directors = key_value.split(":")
    director = directors[1].strip("\n")
    directors = director.split(",") # Derectors name

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
            length = len(languages)
            index = 1
    try:
        languages = languagesOfMovie(index, length, languages) # language
    except IndexError as error:
        index = 0
        length = len(languages)-1
        languages = languagesOfMovie(index, length, languages) # language

    runTime = find_name.find('div', {'class':'subtext'}).time.get_text()
    runtime = runTime.strip()
    split_list = runtime.split()
    hour = split_list[0]
    hour = hour.strip('h')
    if(len(split_list)==2):
        minut = split_list[1]
        minut = minut.strip('min')
        total_min = (int(hour)*60) + int(minut) # Runtime
    else:
        total_min = (int(hour)*60)
    subtext = find_name.find('div', {'class':'subtext'}) #.a.get_text() # Genre
    genre = subtext.text
    genre = genre.strip()
    key_value = genre.split()
    length = len(key_value)-5
    index = 3
    genres = languagesOfMovie(index, length, key_value) # Genre

    # whole details in dictionary formate. :)
    details['name'] = movie_name
    details['director'] = directors
    details['country'] = country_name
    details['language'] = languages
    details['poster_image_url'] = image_url
    details['bio'] = movie_text
    details['runtime'] = total_min
    details['genre'] = genres
    return details

urlList = storeMoviesUrl(moviesData)
url = urlList[0]
movie_details = scrape_movie_details(url)
# pprint (movie_details)
