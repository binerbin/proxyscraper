class ScrapeModel():
    def __init__(self,link,price,product_name="", seller="", image=""):
        self.product_name = product_name
        self.seller = seller
        self.link = link
        self.image = image
        self.price = price
    
    def pretty_print(self):
        return f'[ALERT] {self.product_name} is available for purchase for ${self.price} AT {self.link}'