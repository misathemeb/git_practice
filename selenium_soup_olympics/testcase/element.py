from selenium.webdriver.support.ui import WebDriverWait

class BasePage(object):
    
    
    def __set__(self, obj, value):
        
        driver = obj.driver
        WebDriverWait(driver, 20).until(
            lambda driver: driver.find_element_by_name(self.locator))
        driver.find_element_by_name(self.locator).clear()
        driver.find_element_by_name(self.locator).send_keys(value)
        