


# Python Scraper with BS4 and Asyncio
![Logo](https://i.imgur.com/sXBNSKb.jpg)

This scraper uses asynchronous libraries for efficient scraping, and contains an implemented Amazon base scraper. It also uses proxies to get information quickly and efficiently.

# Requirements

 - Python 3.7 or higher 
 - Beautiful Soup 4 (BS4) library
 - Asyncio library
 - aiohttp library 

You can install these libraries by running:

    pip install beautifulsoup4 asyncio aiohttp

## Usage

 - Clone this repository
 - Install the required libraries using pip
 - Set up your proxy list in proxies.csv
 - Add your product list to products.csv

Run the scraper using the following command:



    python main.py

The scraper will run asynchronously and continuously monitor the products in products.csv. If a product is using the Amazon Buying Options Scraper, the scraper will monitor the available buying options for the product and send an alert if the price drops below a certain threshold.
