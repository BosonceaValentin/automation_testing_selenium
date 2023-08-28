from selenium.webdriver.common.by import By

from base_page import BasePage

class ProductsPage(BasePage):
    AVATAR = (By.XPATH, '//div[contains(text(),"Popescu")]')

    def check_avatar(self):
        assert self.find(self.AVATAR).text == 'Popescu ...'
