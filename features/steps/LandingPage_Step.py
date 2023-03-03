import time
from behave import *
from hamcrest import *
from selenium.webdriver.common.by import By
from features.pages.LandingPageClass import LandingPageClass





@when(u'User mouse hovers on login link')
def step_impl(context):
    context.driver.implicitly_wait(10)
    loginpage = LandingPageClass(context.driver)
    loginpage.mouse_hover()


@step(u'User click on login button')
def step_impl(context):
    context.driver.implicitly_wait(10)
    loginbutton = LandingPageClass(context.driver)
    loginbutton.click_login_button()


