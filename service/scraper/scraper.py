from service.driver.firefox import FirefoxDriver
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, scraper):
        self.scraper = scraper

    def crawl(self, first_page_url):
        self.scraper.start_crawl(first_page_url)
