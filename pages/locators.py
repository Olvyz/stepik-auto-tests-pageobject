from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BOOK_PRICE = (By.XPATH, "//*[@class ='col-sm-6 product_main']/p[@class='price_color']")
    BOOK_NAME = (By.XPATH, "//*[@class ='col-sm-6 product_main']/h1")
    BOOK_NAME_ALERT = (By.XPATH, "//*[@id='messages']/div[1]/div[1]/strong")
    BOOK_PRICE_ALERT = (By.XPATH, "//*[@id='messages']/div[3]/div[1]/p/strong")
