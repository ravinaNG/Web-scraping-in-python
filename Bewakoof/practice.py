import requests
from bs4 import BeautifulSoup
from pprint import pprint

def scrapeDetailsOfTshirts(data):
    detailsList = []
    productGrid = data.find('div', {'class':'productGrid'})
    num = 0
    sum = 1
    for oneTshirt in productGrid:
        sum = sum + 1
        detailsOfOne = {}
        if "0" in oneTshirt.text:
            continue
        productCardBox = oneTshirt.find('div', {'class':'productCardBox'})
        tShirtUrl = 'https://www.bewakoof.com' + oneTshirt.a['href'] # T-shirt Url
        # pprint (tShirtUrl)

        productCardImg = productCardBox.find('div', {'class':'productCardImg false'})
        # for image in productCardImg:
        try:
            img = productCardImg.find('img')
            imgUrl = img['src'] # img url
            # pprint (imgUrl)
        except:
            style = productCardImg.find('div', {'class':''})
            # pprint(style)
            img = style.img
            pprint (img)
            # imgUrl = img['src'] # img url
            # pprint (imgUrl)

        productCardDetail = productCardBox.find('div', {'class':'productCardDetail'})
        name = productCardDetail.find('h3').get_text() # T-shirt name
        # pprint (name)

        productPriceBox = productCardDetail.find('div', {'class':'productPriceBox'})
        loyaltyPriceBox = productPriceBox.find('div', {'class':'loyaltyPriceBox'})
        price = int(loyaltyPriceBox.find('h6').b.get_text()) # Price
        # pprint (price)

        detailsOfOne['T-shirt_Url'] = tShirtUrl
        detailsOfOne['img_url'] = imgUrl
        detailsOfOne['name'] = name
        detailsOfOne['price'] = price

        detailsList.append(detailsOfOne)
        pprint (detailsOfOne)
        num = num + 1
    print (sum)
# pprint (len(productGrid))
    return detailsList

url = "https://www.bewakoof.com/men-clothing"
response = requests.get(url).content
soup = BeautifulSoup(response, 'html5lib')
details = scrapeDetailsOfTshirts(soup)
# pprint (details)