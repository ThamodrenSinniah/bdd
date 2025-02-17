from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os

USER_EMAIL = os.getenv("USER_EMAIL")
USER_PASSWORD = os.getenv("USER_PASSWORD")


@given('I am on the login page')
def located_on_login_page(context):
    context.driver.get("http://127.0.0.1:8080")

@when('I enter valid credentials')
def enter_valid_credentials(context):
    wait = WebDriverWait(context.driver, 10)

    username_field = wait.until(EC.presence_of_element_located((By.ID, "username")))
    password_field = wait.until(EC.presence_of_element_located((By.ID, "password")))
    login_button = wait.until(EC.presence_of_element_located((By.ID, "login-btn")))

    username_field.send_keys(USER_EMAIL)
    password_field.send_keys(USER_PASSWORD)
    login_button.click()


@when('I enter invalid credentials')
def enter_invalid_credentials(context):
    wait = WebDriverWait(context.driver, 10)

    username_field = wait.until(EC.presence_of_element_located((By.ID, "username")))
    password_field = wait.until(EC.presence_of_element_located((By.ID, "password")))
    login_button = wait.until(EC.presence_of_element_located((By.ID, "login-btn")))

    username_field.send_keys("thamo")
    password_field.send_keys("wrong-password")
    login_button.click()


@then('I am logged in')
def successfully_logged_in(context):
    wait = WebDriverWait(context.driver, 10)

    message_banner = wait.until(EC.presence_of_element_located((By.ID, "banner")))
    message_banner_class = message_banner.get_attribute("class")
    assert "success" in message_banner_class


@then('I see an error message')
def see_error_message(context):
    wait = WebDriverWait(context.driver, 10)

    message_banner = wait.until(EC.presence_of_element_located((By.ID, "banner")))
    message_banner_class = message_banner.get_attribute("class")
    assert "error" in message_banner_class




