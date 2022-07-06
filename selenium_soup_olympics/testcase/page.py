
from element import BasePage
from locator import MainPageLocators


class MainPage(BasePage):
    
    def _is_title_matches(self):
        return "Olympedia" in self.driver.title
    
    def click_go_button(self):
        element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
        element.click()
        
class SearchResultsPage(BasePage):
    
    def is_results_found(self):
        return "no results found" not in self.driver.page_source