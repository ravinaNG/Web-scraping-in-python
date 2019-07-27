from first_task import data_in_formate as movie_data
from pprint import pprint
# pprint (movie_data)
end = 1950
dict_of_list = {}
index = 0
current_decade = 2020
for index in movie_data:
    if(end == current_decade):
        break
    start = end
    end = start + 10
    years_list = []
    for year in movie_data :
        if(year['year'] >= start and year['year'] < end):
            years_list.append(index)
        # year = year + 1
    dict_of_list[start] = years_list
    # index = index + 1
pprint (dict_of_list)








# while (index < len(movie_data)):
#     if(end == current_decade):
#         break
#     start = end
#     end = start + 10
#     years_list = []
#     year = 0
#     while (year < len(movie_data)):
#         if(movie_data[year]['year'] >= start and movie_data[year]['year'] < end):
#             years_list.append(movie_data[year])
#         year = year + 1
#     dict_of_list[start] = years_list
#     index = index + 1
# pprint (dict_of_list)
