import fourth_task
import twelthTask
from fourth_task import urlList as moviesUrl
from pprint import pprint

movieUrl = moviesUrl[22]
movieDetails = fourth_task.scrape_movie_details(movieUrl)
cast = twelthTask.scrape_movie_cast(movieUrl)
movieDetails["cast"] = cast
pprint (movieDetails)
