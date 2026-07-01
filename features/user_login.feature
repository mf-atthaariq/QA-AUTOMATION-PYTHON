@ui @regression
Feature: SauceDemo User Authentication Gate
  As a registered user
  I want to log into the SauceDemo application
  So that I can access the e-commerce inventory dashboard

  Scenario: User successfully logs in with valid standard credentials
    Given the user navigates to the SauceDemo login page
    When the user enters username "standard_user" and password "secret_sauce"
    And clicks the login submit button
    Then the user should be redirected to the inventory dashboard page
