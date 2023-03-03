Feature: MagicBricks Login

  Background:
    Given Chrome Browser is opened and Magic bricks website is opened
    When User mouse hovers on login link
    And User click on login button


  Scenario: Validate that user can navigate to the log in page
    Then User able to navigate on to login page


  Scenario: Validate that Next option is clickable
    Then User able to navigate on to login page
    Then User is able to click on the Next button Field


  Scenario:Validate user can click the Need help text link
    Then User able to navigate on to login page
    When User click on the Need help text link
    Then User able to see Forgot Password and Forgot Username options


  Scenario:Validate user can click the About Us text link
    Then User able to navigate on to login page
    When User click on the About Us text link
    Then User able to see the About Us information



  Scenario Outline:Validate Login Functionality with Valid Credentials on Chrome Browser
    Then User able to navigate on to login page
    When User enters the data <valid_data>
    Then User is able to click on the Next button Field
    Then it shows otp page

    Examples:
    | valid_data          |
    | srav123@gmail.com   |
    | 9652959628          |



  Scenario Outline:Validate Login Functionality with Invalid Credentials on Chrome Browser
    Then User able to navigate on to login page
    When User enters the data <invalid_data>
    Then User is able to click on the Next button Field
    Then User able to see an alert message


    Examples:
    | invalid_data         |
    | s1@gmil.com          |
    | 98768                |






















