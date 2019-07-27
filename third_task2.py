from first_task import data_in_formate as movie_data
from pprint import pprint
dicade_dict = {}
module = movie_data[0]['year'] % 10
start_year = movie_data[0]['year'] - module
end_year = movie_data[0]['year'] + 9
for index in (movie_data):
    dict_list = []
    for year in movie_data:
        if(year['year']< end_year and year['year'] >= start_year):
            dict_list.append(year)
    dicade_dict[start_year]=dict_list
    start_year = end_year+1
    end_year = start_year+9  
pprint (dicade_dict) 













# from first_task import data_in_formate as movie_data
# from pprint import pprint
# dicade_dict = {}
# length = len(movie_data)-1
# last_year = movie_data[length]['year']
# module = movie_data[0]['year'] % 10
# start_year = movie_data[0]['year'] - module
# end_year = movie_data[0]['year'] + 9
# index = start_year
# for index in range(start_year, last_year):
#     print (index)
#     if(start_year >= movie_data[length]['year']):
#         break
#     dict_list = []
#     for year in movie_data:
#         if(year['year']< end_year and year['year'] >= start_year):
#             dict_list.append(year)
#     dicade_dict[start_year]=dict_list
#     start_year = end_year+1
#     end_year = start_year+9  
# pprint (dicade_dict) 