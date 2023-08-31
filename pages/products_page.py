from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from base_page import BasePage

class ProductsPage(BasePage):
    AVATAR = (By.XPATH, '//div[contains(text(),"Popescu")]')
    LOGOUT_BUTTON = (By.LINK_TEXT, 'Logout')

    def check_avatar(self):
        assert self.find(self.AVATAR).text == 'Popescu ...'

    def logout(self):
        action = ActionChains(self.browser)
        action.move_to_element(*self.AVATAR).perform()
        self.find(self.LOGOUT_BUTTON).click()
