from TEST_FINAL_TASK.pages.base_page import BasePage
from .locators import ProductPageLocators



class ProductPage(BasePage):
    def click_button_on_buccet(self):
        button = self.browser.find_element(*ProductPageLocators.BUTTON)
        button.click()

    def test_book_title_in_basket_correct(self, link):
        book_title_on_page = self.browser.find_element(*ProductPageLocators.BOOK_TITLE_ON_PAGE).text
        book_title_in_basket = self.browser.find_element(*ProductPageLocators.BOOK_TITLE_IN_BASKET).text

        assert book_title_in_basket == book_title_on_page, f'book titles on {link} is uncorrect!'

    def test_book_price_in_basket_correct(self, link):
        book_price_on_page = self.browser.find_element(*ProductPageLocators.BOOK_PRICE_ON_PAGE).text
        book_price_in_basket = self.browser.find_element(*ProductPageLocators.BOOK_PRICE_IN_BASKET).text

        assert book_price_in_basket == book_price_on_page, f"book prices on {link} is uncorrect"       

    def test_guest_can_add_product_to_basket(self, link):
        self.test_book_title_in_basket_correct(link)
        self.test_book_price_in_basket_correct(link)
