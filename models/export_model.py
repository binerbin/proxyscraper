import requests as rq

class ExportModel():
    def __init__(self,name,data_model,post_url):
        self.name = name
        self.data_model = data_model
        self.post_url = post_url
    
    def post(self):
        rq.post(self.post_url, data=self.data_model)