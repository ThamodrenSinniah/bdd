from behave import use_fixture, fixture
from dotenv import load_dotenv

from features.fixture.browser import ChromeBrowser
from features.fixture.demo_fixture import DemoFixture


load_dotenv()

@fixture
def chrome_browser(context):
    context.driver = ChromeBrowser().get_chrome_driver()
    yield context.driver
    context.driver.quit()

@fixture
def demo_fixture(context):
    context.demo_fixture = DemoFixture().message
    yield context.demo_fixture
    # Cleanup
    context.demo_fixture = None

def before_scenario(context, scenario):
    use_fixture(chrome_browser, context)
