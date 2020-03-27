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
containers = page_soup.findAll("div",{"class":"ProductGrid-inline_7ebuPJ ProductGrid-inline_6uaOga"})

for container in containers:
    product_container = container.findAll("a", {"href": "PrimaryLink_1RLwvm inline-block"})
    price_container = container.findAll("span", {"class": "Price_3HnIBb block"})
    if len(price_container) > 0:
        price = price_container[0].span.text.strip()
        product = product_container[0].span.text.strip()

    print("Product: " + product)
    print("Price: " + price)
    print("")
