import os
import sys
import time
import requests
import threading


from src.constants import VERSION, AMOUNT_THREADS, START_CODE, END_CODE, COLLECT_ONLY
from src.logger import create_links_file, log_link
from src.driver import get_driver
from src.args import parse_args


os.chdir(os.path.dirname(os.path.abspath(__file__)))
starttime = time.strftime("%y-%m-%d_%H:%M:%S")

if not os.path.isdir("links"):
    os.mkdir("links")

if len(sys.argv) > 1:
    AMOUNT_THREADS = parse_args(sys.argv[1:])

print("\033c")
print(f"classpoint-scanner v{VERSION}\nStarting search now...\n")

create_links_file(starttime)


def search_code(c, driver):
    data = requests.get(
        f"https://apitwo.classpoint.app/classcode/region/byclasscode?classcode={c}"
    )

    if data.status_code != 200:
        return

    res_data = data.json()

    if COLLECT_ONLY not in res_data["presenterEmail"]:
        return

    driver.get(f"https://www.classpoint.app/?code={c}")

    time.sleep(1)

    try:
        driver.find_element(
            "xpath", '//*[@id="root"]/div/div[1]/div[3]/div/div/div[2]/div[2]/button'
        ).click()
    except:
        print(f"Error for {c}: Class code next button not found\n")
        return

    time.sleep(1)

    try:
        name_input = driver.find_element("xpath", '//*[@id="standard-basic"]')
        name_input.send_keys("​")
    except:
        print(f"Error for {c}: Name input not found.\n")
        return

    time.sleep(1)

    try:
        driver.find_element(
            "xpath", '//*[@id="root"]/div/div[1]/div[3]/div/div/div[4]/button'
        ).click()
    except:
        print(f"Error for {c}: Join button not found.\n")
        return

    time.sleep(1)

    try:
        image_element = driver.find_element(
            "xpath",
            '//*[@id="root"]/div/div[1]/div[2]/div/div/div[1]/div/div[1]/div/div[1]/div/img',
        )

        image_url = image_element.get_attribute("src")
        if image_url == "":
            print(f"Error for {c}: No slideshow found.\n")
            return

        log_link(c, res_data["presenterEmail"], starttime)
    except:
        print(f"Error for {c}: Not in slideshow.\n")
        return


def search_codes(start, end, driver, thread_no):
    for code in range(start, end):
        search_code(code, driver)

    print(
        f"Search completed for thread {thread_no}, searching from {start} to {end}.\nLinks saved to links.txt\n"
    )


code = START_CODE
threads = []

thread_increment = (END_CODE - START_CODE) // AMOUNT_THREADS

for i in range(AMOUNT_THREADS):
    driver = get_driver()

    thread = threading.Thread(
        target=search_codes, args=(code, code + thread_increment, driver, i + 1)
    )
    thread.daemon = True

    threads.append(thread)

    code += thread_increment

for thread in threads:
    thread.start()

while True:
    time.sleep(1)
