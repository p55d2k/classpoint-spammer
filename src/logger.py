def create_links_file(starttime):
    # open/create the file in write mode
    with open(f"links.txt", "w") as f:
        f.write(f"Last updated: {starttime}\n\n")


def log_link(code, email):
    with open(f"links.txt", "a") as f:
        f.write(f"Email: {email}\nhttps://www.classpoint.app/?code={code}\n\n")

    print("Class code found: " + str(code))
    print("Link saved.\n")
