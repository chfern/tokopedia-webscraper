from service.scraper.scraper import Scraper
from service.scraper.tokopedia_scraper import TokopediaScraper
from service.scraper.bukalapak_scraper import BukalapakScraper
from service.jsonencoder import JsonEncoder
import requests
import json

shops_response = requests.get(url="http://localhost:8000/api/shop")
shops = json.loads(shops_response.content)['shops']

scrap_requests_response = requests.get(url="http://localhost:8000/api/scraprequest?approval_status=A&finalized=false")
scrap_requests = json.loads(scrap_requests_response.content)['scrap_requests']

def add_shop_id_to_item(item, shop_id):
    item.shop_id = shop_id
    return item

scrapped_items = {}

for scrap_request in scrap_requests:
    shoe_to_scrap = scrap_request['name']
    min_price_threshold = scrap_request['min_price_threshold']
    scrap_request_id = scrap_request['id']

    items = []

    for shop in shops:
        shop_name = shop['name'].lower().strip()
        if(shop_name == "tokopedia"):
            tokopedia_scraper = Scraper(TokopediaScraper(min_price_threshold))
            item_list = tokopedia_scraper.crawl("https://www.tokopedia.com/search?ob=5&st=product&q={}".format(shoe_to_scrap))
            items.extend([add_shop_id_to_item(x, shop['id']) for x in item_list])
            pass
        elif(shop_name == "bukalapak"):
            bukalapak_scraper = Scraper(BukalapakScraper(min_price_threshold))
            item_list = bukalapak_scraper.crawl("https://www.bukalapak.com/products/s?page=1&search[hashtag]=&search[keywords]={}&search[sort_by]=rating_float%3Adesc&utf8=%E2%9C%93".format(shoe_to_scrap))
            items.extend([add_shop_id_to_item(x, shop['id']) for x in item_list])
            pass

    scrapped_items[scrap_request_id] = items

    scrap_result_json = json.dumps({ "payload": scrapped_items }, cls=JsonEncoder)
    print(scrap_result_json)
    response = requests.post(url="http://localhost:8000/api/scraprequest", data=scrap_result_json)
    print(response)
    scrapped_items = {}

# scrap_result_json = json.dumps({ "payload": scrapped_items }, cls=JsonEncoder)
# print(scrap_result_json)
# response = requests.post(url="http://localhost:8000/api/scraprequest", data=scrap_result_json)
# print(response)

# tokopedia_scraper = Scraper(TokopediaScraper())
# item_list = tokopedia_scraper.crawl("https://www.tokopedia.com/search?ob=5&st=product&q=yeezy")
# print("Item List : {}".format(item_list))
# tokopedia_scraper.to_csv(TokopediaScraper.folder_name, "yeezy", item_list)

# bukalapak_scraper = Scraper(BukalapakScraper())
# item_list = bukalapak_scraper.crawl("https://www.bukalapak.com/products/s?page=1&search[hashtag]=&search[keywords]=yeezy&search[sort_by]=rating_float%3Adesc&utf8=%E2%9C%93")
# print("Item List : {}".format(item_list))
