class Product():
    def __init__(self, name, link, customer_link, alert_price, scraper, image=""):
        self.name = name
        self.link = link
        self.customer_link = customer_link
        self.alert_price = alert_price
        self.scraper = scraper
        self.image = image
        self.is_selling = False
    
