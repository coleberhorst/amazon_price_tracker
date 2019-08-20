import requests
from bs4 import BeautifulSoup


HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Brave Chrome/76.0.3809.100 Safari/537.36"}
AMAZON_DIVS = {"title": "productTitle", "price": "priceblock_ourprice"}


def product_info(url):
    page = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(page.content, 'html.parser')
    soup2 = BeautifulSoup(soup.prettify(), "html.parser")

    title = soup2.find(id='productTitle').get_text().strip()
    price = soup2.find(id="priceblock_ourprice").get_text()
    price = float(price[1:])
    return title, price



URL = 'https://www.amazon.com/SiliconDust-HDHomeRun-HDHR5-2US-Certified-Refurbished/dp/B07GL4VK1H/ref=pd_ybh_a_32?_encoding=UTF8&psc=1&refRID=8BR7K8NFEM2F6XYAKKQW'
print(product_info(URL))