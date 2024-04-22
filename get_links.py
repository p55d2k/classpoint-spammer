import requests

code = 0

with open("links.txt", "w") as f:
    f.write("")

codes = []

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
    codes.append(code)
    save_link(code)
    code += 1

print(f"class codes found: {codes}")
