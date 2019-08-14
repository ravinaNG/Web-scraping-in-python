import requests
import json
from bs4 import BeautifulSoup
import json.decoder
import json.encoder
res = requests.get("https://www.geeksforgeeks.org/working-with-json-data-in-python/") 
var = json.loads(res.text) 
# var = BeautifulSoup(res.text, 'html5lib')
print (var)