import requests 
from bs4 import BeautifulSoup 

class historicScraper():

    def __init__(self, url,subdomain):
            self.url = url 
            self.subdomain = subdomain 
            # self.data = []
            # self.storeobject = StoreService(os.getcwd(), "stocks.csv")

    