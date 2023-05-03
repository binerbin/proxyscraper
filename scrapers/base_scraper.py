

# ------------------------------------------------------
# Base class for scraping. DON'T CHANGE THIS FILE
#
# __author__ = 'Youssef Haddara'
# ------------------------------------------------------

class BaseScraper:

    def build(self, data):
        """
        Builds the scraper and imports information
        @param data: Data that can be stored in the class
        """

    def scrape(self):
        """
        Fetches a url and scrapes data
        @param link: URL Link that is scraped
        """
        pass

    def parse(self, data):
        """
        Parses the information in a system-friendly manner
        @param data: Request response
        """
        pass

    def export(self):
        """
        Sends out the information to external sources
        """