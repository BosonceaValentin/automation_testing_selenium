from browser import Browser

class BasePage(Browser):
    BASE_URL = 'https://www.evomag.ro/'
    LOGIN_PAGE = 'https://www.evomag.ro/client/auth'

    def find(self, selector):
        return self.browser.find_element(*selector)