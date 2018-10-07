from service.scraper.scraper import Scraper
from service.scraper.tokopedia_scraper import TokopediaScraper
tokopedia_scraper = Scraper(TokopediaScraper())
item_list = tokopedia_scraper.crawl("https://www.tokopedia.com/search?ob=5&st=product&q=photoshop")
print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
print("Item List : {}".format(item_list))
