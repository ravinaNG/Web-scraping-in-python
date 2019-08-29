import requests
from bs4 import BeautifulSoup
from pprint import pprint

def scrapeDetailsOfTshirts(data):
    detailsList = []
    productGrid = data.find('div', {'class':'productGrid'})
    num = 1
    for oneTshirt in productGrid:
        detailsOfOne = {}
        num = num + 1
        print (num)
        try:
            tShirtUrl = 'https://www.bewakoof.com' + oneTshirt.a['href'] # T-shirt Url

            productCardImg = oneTshirt.find('div', {'class':'productCardImg false'})
            img = productCardImg.find('img')
            imgUrl = img['src'] # img url

            productCardDetail = oneTshirt.find('div', {'class':'productCardDetail'})
            name = productCardDetail.find('h3').get_text() # T-shirt name

            productPriceBox = productCardDetail.find('div', {'class':'productPriceBox'})
            loyaltyPriceBox = productPriceBox.find('div', {'class':'loyaltyPriceBox'})
            price = int(loyaltyPriceBox.find('h6').b.get_text()) # Price

            detailsOfOne['T-shirt_Url'] = tShirtUrl
            detailsOfOne['img_url'] = imgUrl
            detailsOfOne['name'] = name
            detailsOfOne['price'] = price

            detailsList.append(detailsOfOne)
        except:
            continue
    # pprint (len(productGrid))
    return detailsList

url = "https://www.bewakoof.com/men-clothing"
response = requests.get(url).content
soup = BeautifulSoup(response, 'html5lib')
details = scrapeDetailsOfTshirts(soup)
# pprint (details)