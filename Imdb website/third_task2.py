from first_task import data_in_formate as movie_data
from pprint import pprint
# pprint (movie_data)
def yearsList(data):
    yearList = []
    for year in data:
        yearList.append(year['year'])
    return yearList

def maxYear(yearList):
    maxNum = yearList[0]
    for index in range(len(yearList)):
        if(yearList[index] > maxNum):
            maxNum = yearList[index]
    return (maxNum)

def miniYear(yearList):
    miniNum = yearList[0]
    for index in range(len(yearList)):
        if(yearList[index] < miniNum):
            miniNum = yearList[index]
    return (miniNum)

def group_by_decade(data, maxYear, miniYear):
    dicade_dict = {}
    lastDigitOfYear = miniYear%10
    miniYear = miniYear - lastDigitOfYear
    maximumYear = miniYear -1
    for miniYear in range(maxYear):
        if(maximumYear >= maxYear):
            return dicade_dict
        dict_list = []
        minimumYear = maximumYear + 1
        maximumYear = minimumYear + 9
        miniYear = maximumYear
        for year in movie_data:
            if(year['year']< maximumYear and year['year'] >= minimumYear):
                dict_list.append(year)
        dicade_dict[minimumYear]=dict_list

yearsList = yearsList(movie_data)
maxYear = maxYear(yearsList)
miniYear = miniYear(yearsList)
decadeDict = group_by_decade(movie_data, maxYear, miniYear)
print (maxYear, end = ":-  Maximum year")
print (" ")
print (miniYear, end = ":-  Minimum year")
print (" ")
pprint (decadeDict)

