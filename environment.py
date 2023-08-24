from browser import Browser
from pages.login_page import LoginPage


def before_all(context):
    context.browser_obj = Browser()
    context.login_obj = LoginPage()

def after_all(context):
    context.browser_obj.close()