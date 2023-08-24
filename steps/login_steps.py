from behave import *

@given("I am on the login page")
def step_impl(context):
    context.login_obj.navigate_to_login_page()

@when("I introduce correct username and correct password")
def step_impl(context):
    pass

@when("I click on the login button")
def step_impl(context):
    pass

@then("I can login in the application and I can see the product list")
def step_impl(context):
    pass