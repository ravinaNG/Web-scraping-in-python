import requests
from bs4 import BeautifulSoup
from pprint import pprint

def scrapeDetailsOfTshirts(data):
    detailsList = []
    productGrid = data.find('div', {'class':'productGrid'})

    for oneTshirt in productGrid:
        detailsOfOne = {}
        if "0" in oneTshirt.text:
            continue
        productCardBox = oneTshirt.find('div', {'class':'productCardBox'})
        tShirtUrl = 'https://www.bewakoof.com' + oneTshirt.a['href'] # T-shirt Url

        productCardImg = productCardBox.find('div', {'class':'productCardImg false'})
        img = productCardImg.find('img')
        if (img == None):
            imgUrl = None # not able to scrape data because of type None
        else:
            imgUrl = img['src'] # img url

        productCardDetail = productCardBox.find('div', {'class':'productCardDetail'})
        name = productCardDetail.find('h3').get_text() # T-shirt name

        productPriceBox = productCardDetail.find('div', {'class':'productPriceBox'})
        loyaltyPriceBox = productPriceBox.find('div', {'class':'loyaltyPriceBox'})
        price = int(loyaltyPriceBox.find('h6').b.get_text()) # Price

        detailsOfOne['T-shirt_Url'] = tShirtUrl
        detailsOfOne['img_url'] = imgUrl
        detailsOfOne['name'] = name
        detailsOfOne['price'] = price

        detailsList.append(detailsOfOne)

    return detailsList

url = "https://www.bewakoof.com/men-clothing"
response = requests.get(url).content
soup = BeautifulSoup(response, 'html5lib')
details = scrapeDetailsOfTshirts(soup)
# pprint (details)