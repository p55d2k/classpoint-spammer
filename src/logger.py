def create_links_file(starttime):
    # create the file in write mode
    with open(f"links/links_{starttime}.txt", "w") as f:
        f.write("")


def log_link(code, email, starttime):
    with open(f"links/links_{starttime}.txt", "a") as f:
        f.write(f"Email: {email}\nhttps://www.classpoint.app/?code={code}\n\n")

    print("Class code found: " + str(code))
    print("Link saved.\n")
