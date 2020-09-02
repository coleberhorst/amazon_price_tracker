import requests
from bs4 import BeautifulSoup


HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Brave Chrome/76.0.3809.100 Safari/537.36"}
WISHLISTS = {
                "Wishlist": "https://www.amazon.com/hz/wishlist/ls/3S7A4JE45XKIU?ref_=wl_share",
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

total = 0
for key, w in WISHLISTS.items():
    print(key, sep="\n")
    for item in wishlist_links(w):
        title, price = product_info(item)
        try:
            total += float(price)
        except ValueError:
            pass
        print(title, price)
print("Total: ", total)

# TODO include links
# TODO price data structure
# TODO include images
# TODO price history
# TODO config file
# TODO graphs and databases
# TODO include products no longer sourced
# TODO 3rd party, used and regular pricing