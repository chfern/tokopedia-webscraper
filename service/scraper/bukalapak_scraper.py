"""
Scraps information per-page
"""
from service.driver.firefox import FirefoxDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from common.base.item import Item
from bs4 import BeautifulSoup
import re

from service.dom import scrollscan_page

class BukalapakScraper:
    base_url = 'https://www.bukalapak.com'
    folder_name = "bukalapak"
    max_page = 10

    def __init__(self, min_price_threshold):
        self.min_price_threshold = min_price_threshold

    def scrap_items(self, soup):
        item_list = []
        list_items = soup.find_all("li", {"class": "col-12--2"})

        for list_item in list_items:
            try:
                product_desc_div = list_item.find("div", {"class": "product-description"})

                product_title = product_desc_div.find("h3").find("a").attrs['title']
                product_page_url = product_desc_div.find("h3").find("a").attrs['href']
                product_price = product_desc_div.find("div", {"class": "product-price"}).find("span").find("span", {"class": "amount"}).text
                product_price = int(product_price.replace('.', ''))
                product_rating_span = product_desc_div.find("div", {"class": "product__rating"}).find("span", {"class": "rating"})
                product_rating = 0
                if product_rating_span != None:
                    product_rating = product_rating_span.attrs['title']

                product_seller_div = product_desc_div.find("div", {"class": "product-seller"})
                product_location = product_seller_div.find("div").find("div", {"class": "user-city"}).find("span").text
                product_seller = product_seller_div.find("div").find("h5").find("a").text
                product_media_div = list_item.find("div", { "class": "product-card" }).find("article").find("div", {"class": "product-media"})
                product_img_url = product_media_div.find("a").find("picture").find("img", {"class": "product-media__img"}).attrs['data-src']
                if(product_price >= self.min_price_threshold):
                    item_list.append(Item(product_title, product_price, product_seller, product_img_url, product_page_url, product_location, product_rating))
            except Exception as e:
                print(e)

        return item_list


    def get_current_search_pagination_elems(self, soup):
        pagination_button_elems = soup.find_all('a', {'href': re.compile(r'/products/s*')})
        pagination_buttons = []
        for pagination_button_elem in pagination_button_elems :
            try:
                int(pagination_button_elem.text)
                pagination_buttons.append(pagination_button_elem)
            except ValueError:
                pass
        return pagination_buttons

    def start_crawl(self, first_page_url):
        item_list = []
        driver = FirefoxDriver().driver
        driver.get(first_page_url)

        curr_page = 1

        has_next_page = True
        while has_next_page and curr_page < BukalapakScraper.max_page :
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "fbpixel")))
            scrollscan_page(driver)

            soup = BeautifulSoup(driver.page_source, "html")

            items = self.scrap_items(soup)
            item_list.extend(items)

            pagination_button_elems = self.get_current_search_pagination_elems(soup)
            has_next_page = False
            for pagination_button_elem in pagination_button_elems:
                if int(pagination_button_elem.text) == (curr_page + 1):
                    driver.get(BukalapakScraper.base_url + pagination_button_elem.attrs['href'])
                    curr_page += 1
                    has_next_page = True
                    break

        return item_list
