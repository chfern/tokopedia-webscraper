from service.scraper.scraper import Scraper
from service.scraper.tokopedia_scraper import TokopediaScraper
tokopedia_scraper = Scraper(TokopediaScraper())
item_list = tokopedia_scraper.crawl("https://www.tokopedia.com/search?ob=5&st=product&q=laravel&page=3")
print("Item List : {}".format(item_list))
tokopedia_scraper.to_csv(TokopediaScraper.folder_name, "laravel", item_list)
