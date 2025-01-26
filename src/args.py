from src.constants import VERSION

import sys
import requests


def parse_args(args):
    if args[0] == "-h":
        print(
            """Usage: python3 main.py [OPTIONS]
    
Options:
    -h, --help\t\t\tShow this help message and exit
    -o, --output\t\tOutput file name and exit
    -v, --version\t\tShow program's version number and exit
    -t, --threads\t\tSet the amount of threads to use
    -c, --code [class code]\tCheck if a class code is valid and exit
    
If no options are provided, the program will run with default settings."""
        )
        sys.exit(0)
    elif args[0] == "-o" or args[0] == "--output":
        print("Output file name: /links/links_{current_datetime}.txt")
        sys.exit(0)
    elif args[0] == "-v" or args[0] == "--version":
        print(f"classpoint-scanner v{VERSION}")
        sys.exit(0)
    elif args[0] == "-t" or args[0] == "--threads":
        if len(args) < 2:
            print("Invalid option. Use -h or --help for help.")
            sys.exit(1)
        elif args[1].isnumeric():
            return max(min(int(args[1]), 128), 1)
        else:
            print("Invalid option. Use -h or --help for help.")
            sys.exit(1)
    elif args[0] == "-c" or args[0] == "--code":
        if len(args) < 2:
            print("Invalid option. Use -h or --help for help.")
            sys.exit(1)
        if (
            requests.get(
                f"https://apitwo.classpoint.app/classcode/region/byclasscode?classcode={args[1]}"
            ).status_code
            != 200
        ):
            print(f"Class code {args[1]} is invalid.")
            sys.exit(1)
        else:
            print(f"Class code {args[1]} is valid.")
            sys.exit(0)
    else:
        print("Invalid option. Use -h or --help for help.")
        sys.exit(1)
