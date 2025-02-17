from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService

class ChromeBrowser:
    def __init__(self):
        self.browser_type = "chrome"
        self.driver_path = ChromeDriverManager().install()
        self.options = self._set_chrome_options()

    @staticmethod
    def _set_chrome_options():
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.page_load_strategy = "normal"
        chrome_options.add_argument("--lang=en")
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--kiosk")
        chrome_options.add_experimental_option("extensionLoadTimeout", 20000)
        chrome_options.add_experimental_option("detach", True)
        chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--disable-software-rasterizer")
        chrome_options.add_argument("--ignore-certificate-errors")
        chrome_options.add_argument("--ignore-certificate-errors")  # Ignore SSL warnings
        chrome_options.add_argument("--disable-web-security")  # Disable same-origin policy
        chrome_options.add_argument("--allow-running-insecure-content")
        return chrome_options

    def get_chrome_driver(self):
        return webdriver.Chrome(
            service=ChromeService(executable_prath=self.driver_path),
            options=self.options,
        )