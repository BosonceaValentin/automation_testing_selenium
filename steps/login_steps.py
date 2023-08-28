from behave import *

@given("I am on the login page")
def step_impl(context):
    context.login_obj.navigate_to_login_page()
    context.login_obj.accept_cookies()

@when("I introduce correct username and correct password")
def step_impl(context):
    context.login_obj.insert_correct_username()
    context.login_obj.insert_correct_password()


@when("I click on the login button")
def step_impl(context):
    context.login_obj.click_login_button()

@then("I can login in the application and I can see the product list")
def step_impl(context):
    context.products_obj.check_avatar()