from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

url = input("Target URL: ")

my_url = url

# Open connection and grabs page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# html parser
page_soup = soup(page_html, "html.parser")

# grabs each product
containers = page_soup.findAll("div",{"class":"styles__StyledDetailsWrapper-e5kry1-8 dnTOUV h-display-flex h-flex-direction-col flex-grow-one full-width"})

for container in containers:
    product_container = container.findAll("a", {"class": "Link-sc-1khjl8b-0 styles__StyledTitleLink-e5kry1-5 cPukFm h-display-block h-text-bold h-text-bs flex-grow-one"})
    price_container = container.findAll("span", {"class": "h-text-bs"})
    if len(price_container) > 0:
        price = price_container[0].span.text.strip()
        product = product_container[0].span.text.strip()
        print("Product: " + product)
        print("Price: " + price)
        print("")
