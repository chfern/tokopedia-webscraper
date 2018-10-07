from service.scraper.scraper import Scraper
from service.scraper.tokopedia_scraper import TokopediaScraper
tokopedia_scraper = Scraper(TokopediaScraper())
tokopedia_scraper.crawl("https://www.tokopedia.com/search?ob=5&st=product&q=photoshop")
