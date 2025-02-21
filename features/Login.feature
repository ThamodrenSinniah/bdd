Feature: Login
  A basic login functionality

  Background: Located in the login page
    Given I am on the login page

  Scenario: I login with valid credentials
    When I enter valid credentials
    Then I am logged in

  Scenario: I login with invalid credentials
    When I enter invalid credentials
    Then I see an error message