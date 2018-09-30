import bs4
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
import pandas as pd

from bs4 import BeautifulSoup

search_queries = [
    "yeezy",
    "air max"
]

url = "https://www.tokopedia.com/search?st=product&q=yeezy"

# New browser session
profile = webdriver.FirefoxProfile()
profile.set_preference("javascript.enabled", True)
driver = webdriver.Firefox(profile)
driver.implicitly_wait(30)
driver.get(url)
driver.page_source
soup = BeautifulSoup(driver.page_source, "html")

all = soup.find_all("div", {"class": "pcr"})

for product_cell in all :
    product_title_elems = product_cell.find_all("h3")
    if len(product_title_elems) > 0:
        product_title = product_title_elems[0].text
        print(product_title)

    product_price_elems = product_cell.find_all("span", {"itemprop": "price"})
    if len(product_price_elems) > 0 :
        product_price = product_price_elems[0].find("span").text
        print(product_price)

    offers_elem = product_cell.find("div", {"itemprop": "offers"})
    print(offers_elem)
    offers_detail_elems = offers_elem.find_all("div")
    if len(offers_detail_elems) > 1 :
        place_elems = offers_detail_elems[2]
        place = place_elems.find("span").text
        place
        rating_elems = offers_detail_elems[3]
        rating_with_brackets = rating_elems.find("span").text
        rating = rating_with_brackets.replace("(", "").replace(")", "")
        rating = int(rating)
