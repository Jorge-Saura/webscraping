import requests 
from bs4 import BeautifulSoup 
import csv 


class DetailScraper():

    def __init__(self):
            self.url = "https://www.bolsamadrid.es"
            self.data = []

    def __getPrizeTable(self, soup):
        table = soup.find(id='ctl00_Contenido_tblPrecios') 
        items = table.find_all('tr')

        #get only two first rows:
        row1= items[0]
        row2 = items[1]


        headers=[]
        values=[]

        for h in row1.find_all('th'):
            headers.append(h.contents[0])
        for p in row2.find_all('td'):
            values.append(p.contents[0])

        return headers, values

    def __getValuesTable(self, soup):
        table = soup.find(id='ctl00_Contenido_tblValor') 
        row = table.find('tr')        #it only has one row
        cells = row.find_all('td')

        headers=[]
        values=[]
        headers.append(cells[0].contents[0].replace("\xa0", ""))
        values.append(cells[1].contents[0].replace("\xa0", ""))

        headers.append(row.find(id='ctl00_Contenido_TickerEtq').contents[0].replace("\xa0", ""))
        values.append(row.find(id='ctl00_Contenido_TickerDat').contents[0].replace("\xa0", ""))

        headers.append(row.find(id='ctl00_Contenido_NominalEtq').contents[0].replace("\xa0", ""))
        values.append(row.find(id='ctl00_Contenido_NominalDat').contents[0].replace("\xa0", ""))

        headers.append(row.find(id='ctl00_Contenido_MercadoEtq').contents[0].replace("\xa0", ""))
        values.append(row.find(id='ctl00_Contenido_MercadoDat').contents[0].replace("\xa0", ""))  

        headers.append(row.find(id='ctl00_Contenido_CapAdmEtq').contents[0].replace("\xa0", ""))
        values.append(row.find(id='ctl00_Contenido_CapAdmDat').contents[0].replace("\xa0", ""))

        return headers, values


    def scrapeDetails(self, url):
        page = requests.get(self.url+url) 
        soup = BeautifulSoup(page.text, 'html.parser')    
        
        # Descripción empresa
        headers, values = self.__getValuesTable(soup) 
        # Últimos precios     
        headers2, values2 = self.__getPrizeTable(soup)               

        return headers+headers2, values+values2
        
            
