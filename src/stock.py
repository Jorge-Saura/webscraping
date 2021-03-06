import requests 
from bs4 import BeautifulSoup 
import csv 

from companydetail import DetailScraper

class StockScraper():

    def __internalMethod(self, attr):
        print("Just to try")
        return "nothing"
    
    
    def __init__(self, url,subdomain):
            self.url = url 
            self.subdomain = subdomain 
            self.data = []

    def __getHtml(self, url):
        print("getting: "+ url)
        return requests.get(url) 

    def __getStockTable(self, soup, id):
        table = soup.find(id=id) 
        items = table.find_all('tr') 
        return items

    def __getArrayFromRow(self, row):
        cells = row.find_all('td')
        array = [i.text for i in cells]        
        return array

    def __getLinkURL(self, row):
        link = row.find('a')
        return link.get('href')

    def scrape(self):
        print ("Stocks Web Scraping  from " + "'" + self.url + "'...")

        page = self.__getHtml(self.url+self.subdomain)
        soup = BeautifulSoup(page.text, 'html.parser') 

        stockTable = self.__getStockTable(soup, 'ctl00_Contenido_tblAcciones')
        detailLinks = []
        stockInfo = []

        for row in stockTable: 
            cells = self.__getArrayFromRow(row)            
            if len(cells) != 0:
                detailLinks.append(self.__getLinkURL(row))
                stockInfo.append(cells)

        # print(detailLinks)
        # print(stockInfo)

        #todo: add "stockInfo" information into a file


        details= DetailScraper()

        n=5  #sólo 5 para las pruebas :)
        for link, i in zip(detailLinks, range(n)):
            headers, values = details.scrapeDetails(link)
            print (headers)
            print (values)