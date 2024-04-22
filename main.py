from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time

options = Options()
# options.add_argument("--log-level=3")

driver = webdriver.Chrome(options=options)

driver.get("https://www.classpoint.app/")

code = 9999
while code < 99999:
    try:
        code += 1
        driver.refresh()
        print(f"entering code {code}")
        driver.find_element("id",
            'standard-basic').send_keys(code)
        print("clicked join")
        driver.find_element("xpath",
            '//*[@id="root"]/div/div[1]/div[3]/div/div/div[2]/div[2]/button').click()
    except:
        break

print(f"class code found: {code}")
