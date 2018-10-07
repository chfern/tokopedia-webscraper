from service.driver.firefox import FirefoxDriver
from bs4 import BeautifulSoup
import pandas as pd
import os

class Scraper:
    def __init__(self, scraper):
        self.scraper = scraper

    def crawl(self, first_page_url):
        return self.scraper.start_crawl(first_page_url)

    def to_csv(self, folder_name, csv_name, item_list):
        """
        @item_list : a list of list with items : ["title", "price", "location", "shop_name", "rating", "product_img_url", "product_detail_url"]
        """

        folder_path = "webdata/" + folder_name + "/"
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        headers = ["title", "price", "location", "shop_name", "rating", "product_img_url", "product_detail_url"]
        print("generating csv from itemlist: ")
        print(item_list)
        dfresult = pd.DataFrame(item_list, columns=headers)

        dfresult.to_csv(folder_path + csv_name + ".csv", sep=',')
