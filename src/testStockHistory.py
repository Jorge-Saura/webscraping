import unittest
import os
from bs4 import BeautifulSoup
from stock import StockScraper
from companyhistory import historicScraper
from testfixtures import TempDirectory, compare

class TestHistoricStocks(unittest.TestCase):

    def setUp(self):
        self.url = "https://www.bolsamadrid.es"
        self.domain = "/esp/aspx/Empresas/InfHistorica.aspx?ISIN=ES0125220311&ClvEmis=25220"
        
        pass

    def tearDown(self):
        
        pass


    def test_get_algo(self):
        print('hola')
        
  

 
if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestHistoricStocks)
    unittest.TextTestRunner(verbosity=2).run(suite) 