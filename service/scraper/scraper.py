from service.driver.firefox import FirefoxDriver
from bs4 import BeautifulSoup
import pandas

class Scraper:
    def __init__(self, scraper):
        self.scraper = scraper

    def crawl(self, first_page_url):
        self.scraper.start_crawl(first_page_url)

    def to_csv(self, folder_name, csv_name, item_list):
        """
        @item_list : a list of list with items : ["title", "price", "location", "shop_name", "rating", "product_img_url", "product_detail_url"]
        """
        headers = ["title", "price", "location", "shop_name", "rating", "product_img_url", "product_detail_url"]

        dfresult = pandas.Dataframe(item_list, headers)
