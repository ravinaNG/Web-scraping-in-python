from first_task import data_in_formate as movie_info
from pprint import pprint

print ("*****************second task*********************")
def group_by_year(movie_info):
    year_key = {}
    for index in movie_info:
        year = index['year']
        dict_list = []
        for chaking_dict in movie_info:
            if(year == chaking_dict['year']):
                dict_list.append(chaking_dict)
        year_key[year] = dict_list
    return year_key
pprint (group_by_year(movie_info))