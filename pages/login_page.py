from pages.base_page import BasePage
from pages.locators import LoginPageLocators
import time

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        login_url = self.browser.current_url
        assert "login" in login_url, "This is not Login page"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM),"Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM),"Register form is not presented"

    def register_new_user(self, email, password):
        try:
            input1 = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
            input1.send_keys(email)
            input2 = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD1)
            input2.send_keys(password)
            input3 = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD2)
            input3.send_keys(password)
            button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
            button.click()
        finally:
            time.sleep(5)



