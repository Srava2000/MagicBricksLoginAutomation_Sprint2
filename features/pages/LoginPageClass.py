from selenium.webdriver.common.by import By



class LoginPageClass:


    def __init__(self, driver):
        self.driver = driver


        # Element Locators Values

        self.NextbuttonElement = "//div[@class='web-page']/div[2]/div/div[2]/div[2]/div[2]/button"

        self.NeedHelpLink ="//a[@class='help'][1]"

        self.TextInput = '//input[@id="emailOrMobile"]'

        self.FieldClickElement = "//*[@id='emailOrMobile']"

        self.AboutusElement = "//a[@href='https://m.magicbricks.com/mbs/about.html']"

        self.DataInput= '//input[@name="emailOrMobile"]'

        self.ContinueLink="//button[@onclick='verifyOtp()']"








    # Creating Element Methods


    def click_about_us(self):
        AboutUs = self.driver.find_element(By.XPATH, self.AboutusElement)
        AboutUs.click()

    def click_next_button(self):
        NextButton = self.driver.find_element(By.XPATH, self.NextbuttonElement)
        NextButton.click()

    def click_next_help_link(self):
        NeedHelp = self.driver.find_element(By.XPATH, self.NeedHelpLink)
        NeedHelp.click()

    def enter_TextInput(self,mobilenumber):
        MobileNumberTextbox = self.driver.find_element(By.XPATH, self.TextInput)
        MobileNumberTextbox.send_keys(mobilenumber)

    def click_num_field(self):
        NumberClk=self.driver.find_element(By.XPATH,self.FieldClickElement)
        NumberClk.click()

    def enter_dataInput(self,datavalue):
        dataenter=self.driver.find_element(By.XPATH,self.DataInput)
        dataenter.send_keys(datavalue)

    def click_continue_link(self):
        continueLink=self.driver.find_element(By.XPATH,self.ContinueLink)
        continueLink.click()

    def check_otpWindow_Text(self):
        otpWindowText = self.driver.find_element(By.XPATH, self.ContinueLink).text
        return otpWindowText














