import sys

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
