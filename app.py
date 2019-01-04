from service.scraper.scraper import Scraper
from service.scraper.tokopedia_scraper import TokopediaScraper
from service.scraper.bukalapak_scraper import BukalapakScraper
from service.jsonencoder import JsonEncoder
import requests
import json
import schedule
import time

base_api_url = 'https://urbansneakers.herokuapp.com/'

def scrap_data():
    shops_response = requests.get(url="{}api/shop".format(base_api_url))
    shops = json.loads(shops_response.content)['shops']

    scrap_requests_response = requests.get(url="{}api/scraprequest?approval_status=A&finalized=false".format(base_api_url))
    scrap_requests = json.loads(scrap_requests_response.content)['scrap_requests']

    scrapped_items = {}

    for scrap_request in scrap_requests:
        shoe_to_scrap = scrap_request['name']
        min_price_threshold = scrap_request['min_price_threshold']
        scrap_request_id = scrap_request['id']

        items = []

        for shop in shops:
            shop_name = shop['name'].lower().strip()
            if(shop_name == "tokopedia"):
                tokopedia_scraper = Scraper(TokopediaScraper(int(min_price_threshold)))
                item_list = tokopedia_scraper.crawl("https://www.tokopedia.com/search?ob=5&st=product&q={}".format(shoe_to_scrap))
                items.extend([add_shop_id_to_item(x, shop['id']) for x in item_list])
                pass
            elif(shop_name == "bukalapak"):
                bukalapak_scraper = Scraper(BukalapakScraper(int(min_price_threshold)))
                item_list = bukalapak_scraper.crawl("https://www.bukalapak.com/products/s?page=1&search[hashtag]=&search[keywords]={}&search[sort_by]=rating_float%3Adesc&utf8=%E2%9C%93".format(shoe_to_scrap))
                items.extend([add_shop_id_to_item(x, shop['id']) for x in item_list])
                pass

        scrapped_items[scrap_request_id] = items

        scrap_result_json = json.dumps({ "payload": scrapped_items }, cls=JsonEncoder)
        response = requests.post(url="{}api/scraprequest".format(base_api_url), data=scrap_result_json)
        print(response)
        scrapped_items = {}


def add_shop_id_to_item(item, shop_id):
    item.shop_id = shop_id
    return item


schedule.every(15).minutes.do(scrap_data)

scrap_data()
while True:
    schedule.run_pending()
    time.sleep(1)
