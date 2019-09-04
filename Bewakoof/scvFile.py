import csv
from detailsOfEachTshirt import details

fileName = "demoCsvFile.csv"

with open(fileName, 'w', newline='') as csvFile:
    fileWriter = 