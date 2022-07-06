import unittest
from selenium import webdriver

import page

class OlympediaSearch(unittest.TestCase):
    
    def setup(self):
        print('setup')
        self.driver = webdriver.Safari()
        self.driver.get('http://www.olympedia.org/')
        
        
    def test_title(self):
        mainPage = page.MainPage()
        assert mainPage.is_title_matches()
        
        
        
    def tearDown(self):
        self.driver.close()
        
        
if  __name__ == "__main__":
    unittest.main()

