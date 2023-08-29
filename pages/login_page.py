import time

from selenium.webdriver.common.by import By

from base_page import BasePage

class LoginPage(BasePage):
    USERNAME_BAR = (By.ID, 'LoginClientForm_Email')
    PASSWORD_BAR = (By.ID, 'LoginClientForm_Password')
    LOGIN_BUTTON = (By.CSS_SELECTOR, "input[value='INTRA IN CONT']")
    COOKIES_ACCEPT = (By.CSS_SELECTOR, 'button[class="gdpr-btn btn-1"]')
    INCORRECT_EMAIL_ERROR = (By.CSS_SELECTOR, 'div[class="generic_error_message err1"]')
    def accept_cookies(self):
        self.find(self.COOKIES_ACCEPT).click()

    def navigate_to_login_page(self):
        self.browser.get(self.LOGIN_PAGE)
        time.sleep(3)

    def insert_correct_username(self):
        username = self.find(self.USERNAME_BAR)
        username.send_keys('zalando.lounge34@gmail.com')

    def insert_correct_password(self):
        password = self.find(self.PASSWORD_BAR)
        password.send_keys('zalandolounge34@#')

    def click_login_button(self):
        self.find(self.LOGIN_BUTTON).click()

    def insert_incorrect_username(self):
        username = self.find(self.USERNAME_BAR)
        username.send_keys('blablabla')

    def check_incorrect_email_error(self):
        incorrect_email_error = self.find(self.INCORRECT_EMAIL_ERROR)
        assert incorrect_email_error.text == 'Nu va puteti autentifica! Adresa de email introdusa este invalida!'

