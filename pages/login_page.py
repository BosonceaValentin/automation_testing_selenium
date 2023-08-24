from base_page import BasePage

class LoginPage(BasePage):
    def navigate_to_login_page(self):
        self.browser.get(self.LOGIN_PAGE)