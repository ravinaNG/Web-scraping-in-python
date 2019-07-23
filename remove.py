year = "(9807)"
yea = list(year)
# print (yea)
year = (yea.remove(yea[0]))
year = yea
# print (type(year))
# print (year)
yea = (year.remove(year[4]))
yea = year
# print (yea)
year = ""
index = 0
while (index < len(yea)):
    year = year + yea[index]
    index = index + 1
print (year)
