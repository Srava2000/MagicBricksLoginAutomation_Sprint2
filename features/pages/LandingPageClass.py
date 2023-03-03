from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class LandingPageClass:


    def __init__(self, driver):
        self.driver = driver

        # Element Locators Values
        self.DropdownElement = "//div[@class='mb-header__main__right']/div[2]/a"

        self.loginLinkElement = "//a[@class='mb-login__drop-cta']"

    # Creating Element Methods
    def click_login_button(self):
        login_button = self.driver.find_element(By.XPATH, self.loginLinkElement)
        login_button.click()

        print("Parent window title: " + self.driver.title)

        # get current window handle
        p = self.driver.current_window_handle

        # get first child window
        chwd = self.driver.window_handles

        for w in chwd:
            # switch focus to child window
            if (w != p):
                self.driver.switch_to.window(w)
            continue

    def mouse_hover(self):
        mousehover = self.driver.find_element(By.XPATH, self.DropdownElement)
        action = ActionChains(self.driver)
        action.move_to_element(mousehover)
        action.perform()
