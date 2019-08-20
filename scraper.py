import requests
from bs4 import BeautifulSoup


HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Brave Chrome/76.0.3809.100 Safari/537.36"}
WISHLISTS = {
                "Replacement": "https://www.amazon.com/hz/wishlist/ls/3S7A4JE45XKIU",
                "Clothing": "https://www.amazon.com/hz/wishlist/ls/3P8GNXAAAM2HE",
                "Consumables": "https://www.amazon.com/hz/wishlist/ls/3Q0GBZP6F120Q",
                "Indulgent": "https://www.amazon.com/hz/wishlist/ls/2CQFAZL80VSIC",
                "Secondary": "https://www.amazon.com/hz/wishlist/ls/IE0QAES8RXDH"
            }
AMAZON_DIVS = {"title": "productTitle", "price": "priceblock_ourprice", "wishlist": "g-items"}


def wishlist_links(url):
    page = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(page.content, 'html.parser')
    soup2 = BeautifulSoup(soup.prettify(), "html.parser")
    wishlist = soup2.find_all("div", {"class": "a-row a-size-small"})
    links = []
    for item in wishlist:
        links.append("https://www.amazon.com" + item.find("a", href=True)['href'])
    return links



def product_info(url):
    page = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(page.content, 'html.parser')
    soup2 = BeautifulSoup(soup.prettify(), "html.parser")

    title = soup2.find(id='productTitle').get_text().strip()
    try:
        price = soup2.find(id="priceblock_ourprice").get_text()
    except AttributeError:
        price = "Not Available"
    try:
        price = float(price[1:])
    except ValueError:
        price = "Not Available"
    return title, price


for key, w in WISHLISTS.items():
    print(key, sep="\n")
    for item in wishlist_links(w):
        print(product_info(item))