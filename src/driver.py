from selenium.webdriver.chrome.options import Options
from selenium import webdriver


def get_driver():
    options = Options()

    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--log-level=3")

    driver = webdriver.Chrome(options=options)

    return driver
