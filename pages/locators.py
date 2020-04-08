from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.XPATH, "//button[@name='registration_submit']")

class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BOOK_PRICE = (By.XPATH, "//*[@class ='col-sm-6 product_main']/p[@class='price_color']")
    BOOK_NAME = (By.XPATH, "//*[@class ='col-sm-6 product_main']/h1")
    BOOK_NAME_ALERT = (By.XPATH, "//*[@id='messages']/div[1]/div[1]/strong")
    BOOK_PRICE_ALERT = (By.XPATH, "//*[@id='messages']/div[3]/div[1]/p/strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages>div>div.alertinner")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET = (By.XPATH, "//*[@class='btn-group']/*[@class='btn btn-default']")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    EMPTY_BASKET = (By.XPATH, "//p[contains(text(), 'Your basket is empty')]")
