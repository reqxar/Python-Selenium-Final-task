from TEST_FINAL_TASK.pages.base_page import BasePage
from selenium.common.exceptions import NoAlertPresentException
from .locators import ProductPageLocators
import math



class ProductPage(BasePage):
    def click_button_on_korzina(self):
        button = self.browser.find_element(*ProductPageLocators.BUTTON)
        button.click()




