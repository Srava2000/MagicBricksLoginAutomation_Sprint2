Feature: MagicBricks Login Data


  Scenario:Validate Login Functionality with Valid Credentials on Chrome Browser
    Given Chrome Browser is opened and Magic bricks website is opened
    When User mouse hovers on login link
    Then User click on login button
    And User able to navigate on to login page
    When User enters the data for first dataset
    And User is able to click on the Next button Field for first dataset
    Then it shows otp page


  Scenario:Validate Login Functionality with Invalid Credentials on Chrome Browser
    Given Chrome Browser is opened and Magic bricks website is opened
    When User mouse hovers on login link
    Then User click on login button
    And User able to navigate on to login page
    When User enters the data for second dataset
    And User is able to click on the Next button Field for second dataset
    Then User able to see an alert message
