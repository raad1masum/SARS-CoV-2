from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

url = input("BedBath and Beyond URL: ")

my_url = url

# Open connection and grabs page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# html parser
page_soup = soup(page_html, "html.parser")

# grabs each product
containers = page_soup.findAll("div",{"class":"ProductGrid-inline_7ebuPJ"})

for container in containers:
    product_container = container.findAll("a", {"class": "PrimaryLink_1RLwvm"})
    price_container = container.findAll("span", {"class": "Price_3HnIBb"})
    if len(price_container) > 0:
        price = price_container[0].span.text.strip()
        product = product_container[0].span.text.strip()

    print("Product: " + product)
    print("Price: " + price)
    print("")
