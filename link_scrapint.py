from bs4 import BeautifulSoup

import requests

url = input("Enter a website to extract the URL's from: ")

# url = "bdjobs.com/"

r = requests.get("https://" + url)

data = r.text

soup = BeautifulSoup(data)

for link in soup.find_all('a'):
    print(link.get('href'))
