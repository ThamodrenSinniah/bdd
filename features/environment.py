from behave import use_fixture, fixture
from dotenv import load_dotenv

from features.fixture.browser import ChromeBrowser


load_dotenv()

@fixture
def chrome_browser(context):
    context.driver = ChromeBrowser().get_chrome_driver()
    yield context.driver
    context.driver.quit()


def before_scenario(context, scenario):
    use_fixture(chrome_browser, context)
