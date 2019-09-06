from selenium import webdriver
from pprint import pprint
from bs4 import BeautifulSoup
from detailsOfEachTshirt import scrapeDetailsOfTshirts
import time

url = "https://www.bewakoof.com/men-clothing"
driver = webdriver.Chrome() 
driver.get(url)
SCROLL_PAUSE_TIME = 5

# Get scroll height
last_height = 0 

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")

    if new_height == last_height:
        break
    last_height = new_height

soup = BeautifulSoup(driver.page_source, 'html5lib')
data = scrapeDetailsOfTshirts(soup)
pprint (driver.page_source)
# pprint (data)