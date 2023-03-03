import time
from behave import *
from datafiles import ExcelUtils
from features.utility.ConfigClass import ConfigClass
from features.pages.LoginPageClass import LoginPageClass


@when(u'User enters the {data} for first dataset')
def step_impl(context,data):
    ExcelUtils.get_row_count(ConfigClass.dataFilePath, "Sheet1")
    data = ExcelUtils.read_data(ConfigClass.dataFilePath, "Sheet1", 2, 1)

    dataenter=LoginPageClass(context.driver)
    dataenter.enter_dataInput(data)



@step(u'User is able to click on the Next button Field for first dataset')
def step_impl(context):
    expectedTitle = 'User Login'
    actualTitle = context.driver.title
    print(actualTitle)
    context.driver.implicitly_wait(10)

    nextbutton = LoginPageClass(context.driver)
    nextbutton.click_next_button()

    try:
        if (expectedTitle == actualTitle):
         assert True
         print("Test is passed")
         ExcelUtils.write_data(ConfigClass.dataFilePath, "Sheet1", 2, 2, "Passed")
        else:
         print("Test is failed")
         ExcelUtils.write_data(ConfigClass.dataFilePath, "Sheet1", 2, 2, "Failed")
         assert False
        time.sleep(2)
    finally:
        continueLink=LoginPageClass(context.driver)
        continueLink.click_continue_link()
        time.sleep(2)


@when(u'User enters the {data} for second dataset')
def step_impl(context,data):
    ExcelUtils.get_row_count(ConfigClass.dataFilePath, "Sheet1")
    data = ExcelUtils.read_data(ConfigClass.dataFilePath, "Sheet1", 3, 1)

    dataenter = LoginPageClass(context.driver)
    dataenter.enter_dataInput(data)


@step(u'User is able to click on the Next button Field for second dataset')
def step_impl(context):
        expectedTitle = 'abcd login'
        actualTitle = context.driver.title
        print(actualTitle)

        context.driver.implicitly_wait(10)

        nextbutton = LoginPageClass(context.driver)
        nextbutton.click_next_button()

        try:
            if (expectedTitle == actualTitle):
                assert True
                print("Test is Passed")
                ExcelUtils.write_data(ConfigClass.dataFilePath, "Sheet1", 3, 2, "Passed")
            else:
                print("Test is Failed")
                ExcelUtils.write_data(ConfigClass.dataFilePath, "Sheet1", 3, 2, "Failed")
                assert False
            context.driver.implicitly_wait(10)
        finally:
            continueLink = LoginPageClass(context.driver)
            continueLink.click_continue_link()
            context.driver.implicitly_wait(10)



