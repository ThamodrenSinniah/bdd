import os
import logging

from behave import use_fixture, fixture

from features.fixture.browser import ChromeBrowser

@fixture
def chrome_browser(context):
    context.driver = ChromeBrowser().get_chrome_driver()
    yield context.driver
    context.driver.quit()

def before_scenario(context, scenario):
    use_fixture(chrome_browser, context)
