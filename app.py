from service.scraper.scraper import Scraper
from service.scraper.tokopedia_scraper import TokopediaScraper
from service.scraper.bukalapak_scraper import BukalapakScraper

# tokopedia_scraper = Scraper(TokopediaScraper())
# item_list = tokopedia_scraper.crawl("https://www.tokopedia.com/search?ob=5&st=product&q=yeezy")
# print("Item List : {}".format(item_list))
# tokopedia_scraper.to_csv(TokopediaScraper.folder_name, "yeezy", item_list)

bukalapak_scraper = Scraper(BukalapakScraper())
item_list = bukalapak_scraper.crawl("https://www.bukalapak.com/products/s?page=1&search[hashtag]=&search[keywords]=yeezy&search[sort_by]=rating_float%3Adesc&utf8=%E2%9C%93")
print("Item List : {}".format(item_list))
