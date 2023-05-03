import re
import csv
from models.proxy_model import ProxyModel
from models.product import Product
import os

def htmlPricesToFloat(data):
    result = []
    for listing in data:
        listing = listing.replace(",","")
        data = re.search("\d+.\d+", listing)
        result.append(float(data.group(0)))
    return result

def htmlPriceToFloat(data):
    result = ""
    data = data.replace(",","")
    data = re.search("\d+.\d+", data)
    return float(data.group(0))

def load_proxies_from_csv(file_name):
    proxies = []
    try:
        with open(file_name) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    line_count+= 1
                    continue
                p = row[0].split(":")
                proxy = f"{p[0]}:{p[1]}"
                username = p[2]
                password = p[3]
                proxy_obj = ProxyModel(proxy, username, password)
                proxies.append(proxy_obj)
                line_count += 1
    except:
        raise Exception("Could not load proxies from csv file!")
    else:
        return proxies

def load_products_from_csv(file_name):
    products = []
    try:
        with open(file_name) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    line_count+= 1
                    continue
                name = row[0]
                link = row[1]
                customer_link = row[2]
                alert_price = int(row[3])
                scraper = row[4]
                image = row[5]
                product = Product(name,link,customer_link,alert_price,scraper,image)
                products.append(product)
                line_count += 1
    except:
        raise Exception("Could not load products from csv file!")
    else:
        return products