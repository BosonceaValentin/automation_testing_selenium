from browser import Browser
from pages.login_page import LoginPage
from pages.products_page import ProductsPage


def before_all(context):
    context.browser_obj = Browser()
    context.login_obj = LoginPage()
    context.products_obj = ProductsPage()

def after_all(context):
    context.products_obj.logout()
    context.browser_obj.close()