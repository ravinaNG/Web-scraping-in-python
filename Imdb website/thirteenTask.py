import fourth_task
import twelthTask
from fourth_task import urlList as moviesUrl
from pprint import pprint

def movieDetailsWithCast(url):
    movieDetails = fourth_task.scrape_movie_details(url)
    cast = twelthTask.scrape_movie_cast(url)
    movieDetails["cast"] = cast
    return movieDetails

movieUrl = moviesUrl[22]
detailsWithCast = movieDetailsWithCast(movieUrl)
pprint (detailsWithCast)