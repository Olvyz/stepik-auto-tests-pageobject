from pages.base_page import BasePage
from pages.locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_button.click()

    def should_be_book_name(self):
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        book_name_alert = self.browser.find_element(*ProductPageLocators.BOOK_NAME_ALERT).text
        assert book_name == book_name_alert, "Not the same book"

    def should_be_book_price(self):
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        book_price_alert = self.browser.find_element(*ProductPageLocators.BOOK_PRICE_ALERT).text
        assert book_price_alert == book_price, "Not the same price"
