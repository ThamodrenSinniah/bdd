# Features

This directory contains the feature files for the project. These files are written in Gherkin syntax and are used for behavior-driven development (BDD) testing.

## Directory Structure

- `features/Login.feature`: Contains scenarios for testing the login functionality.

## Writing Feature Files

Feature files should follow the Gherkin syntax, which includes the following keywords:
- `Feature`: A high-level description of a software feature.
- `Background`: Steps that are common to all scenarios in the feature.
- `Scenario`: A specific situation or test case.
- `Given`: The initial context of the scenario.
- `When`: An event or action.
- `Then`: The expected outcome.

## Example

Here is an example of a feature file:

```gherkin
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
```

## Running Tests

Before running the tests, make sure your app is up and running.

Refer to the README in `app/README.md` to start running the app

To run the tests, follow the commands:

1. **Ensure your virtual environment is activated with poetry**
    ```sh
    poetry shell
    ```
2. **Run the behave tests**
    ```sh
      # In the root directory
      # Feel free to change the name of the report folder to whatever you like
      behave -f allure_behave.formatter:AllureFormatter -o reports/
    ```

## View reports

```sh
  allure serve reports/
```