from typing import overload
from scrapers.base_scraper import BaseScraper
from bs4 import BeautifulSoup as bs
from settings import settings
from utils import pointers
from models.product import Product
from models.scrape_model import ScrapeModel
from utils.utils import htmlPriceToFloat
from utils.proxy_manager import ProxyManager
import asyncio
import aiohttp

class Amazon_Buying_Options_Scraper(BaseScraper):

    def __init__(self):
        self.headers = {
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                        'Service-Worker-Navigation-Preload': 'true',
                        'Upgrade-Insecure-Requests': '1',
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
                        }
        self.name = "Amazon Buying Options Scraper: "
        self.product: Product = None
        self.manager = ProxyManager()

    def build(self, product):
        self.product = product

    async def scrape(self):
        try:
            response = await self.manager.fetch(self.product.link, headers=self.headers)
            soup = bs(response, 'html.parser')
        except:
            raise Exception("Error fetching url... timeout? proxy?")
        
        # GET AVAILABLE LISTINGS
        try:
            listings = soup.select(pointers.AMZ_LISTING)
            price = self.parse(listings)
        except:
            raise Exception("Error getting Amazon Buying Options Listings!")

        if not price:
            print("Found nothing!")
            return
        
        if self.product.is_selling:
            return

        result = ScrapeModel(self.product.customer_link, price,product_name=self.product.name)
        self.export(result)
        return result
        
    
    def parse(self, data):
        min_price = 1000000
        ping = False
        try:
            for listing in data:
                price = listing.select(pointers.AMZ_PRICE)[0].text
                price = htmlPriceToFloat(price)
                if price < min_price:
                    min_price = price
                if price < self.product.alert_price:
                    ping = True
        except Exception:
            raise Exception("Error parsing the data!")

        if ping:
            return min_price
        
        self.product.is_selling = False

        return None
    
    async def monitor(self):
        while True:
            try:
                await asyncio.sleep(settings.REQUEST_INTERVAL)
                await self.scrape()
            except asyncio.exceptions.CancelledError as e:
                raise(e)
            except:
                raise Exception(f"{self.name} Error monitoring!")

    async def wait(self, delay):
        await asyncio.sleep(delay)

    def export(self, model: ScrapeModel):
        print(model.pretty_print())
        return 