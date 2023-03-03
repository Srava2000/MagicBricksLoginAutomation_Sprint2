import time
from behave import *
from hamcrest import *
from features.pages.LoginPageClass import LoginPageClass



@given(u'Chrome Browser is opened and Magic bricks website is opened')
def step_impl(context):
    context.driver.implicitly_wait(10)
    expectedTitle = "Real Estate | Property in India | Buy/Sale/Rent Properties | MagicBricks"
    actualTitle = context.driver.title
    print("Page title is " + actualTitle)
    assert_that(expectedTitle, equal_to(actualTitle))



@then(u'User able to navigate on to login page')
def step_impl(context):
    context.driver.implicitly_wait(10)
    expectedTitle = 'User Login'
    actualTitle = context.driver.title
    print("Page title is " + actualTitle)
    assert_that(expectedTitle, equal_to(actualTitle))


@when(u'User enters the data {mobnum}')
def step_impl(context, mobnum):
    context.driver.implicitly_wait(10)
    MobileNumber = LoginPageClass(context.driver)
    MobileNumber.enter_TextInput(mobnum)
    context.driver.implicitly_wait(10)


@then(u'User is able to click on the Next button Field')
def step_impl(context):
    context.driver.implicitly_wait(10)
    nextbutton = LoginPageClass(context.driver)
    nextbutton.click_next_button()


@then(u'it shows otp page')
def step_impl(context):
    context.driver.implicitly_wait(10)
    expectedTitle = 'User Login'
    actualTitle = context.driver.title
    print("Page title is " + actualTitle)
    assert_that(expectedTitle, equal_to(actualTitle))



@when(u'User click on the Need help text link')
def step_impl(context):
    context.driver.implicitly_wait(10)
    needhelp = LoginPageClass(context.driver)
    needhelp.click_next_help_link()


@then(u'User able to see Forgot Password and Forgot Username options')
def step_impl(context):
    context.driver.implicitly_wait(10)
    expectedTitle = 'User Login'
    actualTitle = context.driver.title
    print("Page title is " + actualTitle)
    assert_that(expectedTitle, equal_to(actualTitle))

@then(u'User able to see an alert message')
def step_impl(context):
    context.driver.implicitly_wait(10)
    expectedTitle = 'User Login'
    actualTitle = context.driver.title
    print("Page title is " + actualTitle)
    assert_that(expectedTitle, equal_to(actualTitle))


@when(u'User click on the About Us text link')
def step_impl(context):
    context.driver.implicitly_wait(10)
    aboutUs = LoginPageClass(context.driver)
    aboutUs.click_about_us()

@then(u'User able to see the About Us information')
def step_impl(context):
    context.driver.implicitly_wait(10)
    expectedTitle ='Real Estate in India - Buy, Sell, Rent Residential Apartment, Plot, House, Commercial Properties in India - MagicBricks-Mobile'
    actualTitle = context.driver.title
    print("Page title is " + actualTitle)
    assert_that(expectedTitle, equal_to(actualTitle))






