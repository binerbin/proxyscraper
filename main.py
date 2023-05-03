from models.product import Product
from scrapers.base_scraper import BaseScraper
from scrapers.amz_bo_scraper import Amazon_Buying_Options_Scraper
import asyncio
from models.proxy_model import ProxyModel
from utils import utils
from utils.pointers import SCRAPER_AMAZON_BUYING_OPTIONS
from utils.proxy_manager import ProxyManager

scraper: BaseScraper = None
scraper = Amazon_Buying_Options_Scraper()

proxies = utils.load_proxies_from_csv("proxies.csv")
ProxyManager.loadProxies(ProxyManager, proxies)

async def build_scrapers():
    tasks = []
    responses = ""
    try:
        for product in utils.load_products_from_csv("products.csv"):
            print(product.name)
            if product.scraper == SCRAPER_AMAZON_BUYING_OPTIONS:
                scraper = Amazon_Buying_Options_Scraper()
                scraper.build(product)
                tasks.append(scraper.monitor())
        responses = await asyncio.gather(*tasks)
    except Exception:
        print("Error building scrapers and running them asynchronously !")
    return responses

asyncio.run(build_scrapers())
