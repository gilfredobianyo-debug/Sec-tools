import requests
from bs4 import BeautifulSoup

while True:
    try:
        url = input("Enter a website url: ")
        if not url[-4:].startswith("."):
            raise ValueError("Specify '.com', '.org' etc")
        elif not url.startswith("http"):
            url = "https://" + url
            print(url)
        else:
            print("Searching...")

    except ValueError as e:
        print(f"Error:{e}")
    else:
        print(url)
        break

req = requests.get(url)
html = req.text
print(req.status_code)

soup = BeautifulSoup(html, 'html.parser')
links = soup.find_all('a', href=True)

link_cont = []
accepted_links = []

for a in links:
    href = a.get('href')
    link_cont.append(href)

for item in link_cont:
    if item.startswith("http"):
        accepted_links.append(item)

for item in accepted_links:
    try:
        r = requests.get(item, timeout=5)
        if r.status_code == 200:
            print(f"{item}: \n Working")
        elif r.status_code == 404:
            print(f"{item}: \n Broken")
        else:
            print(f"{item}: \n Status {r.status_code}")
        print('----------------------')
    except:
        print(f"{item}: \n Failed")
        print('----------------------')