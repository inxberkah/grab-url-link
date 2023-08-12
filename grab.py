import requests
from bs4 import BeautifulSoup

url = input("Input url: ")

response = requests.get(url)
html_content = response.text

soup = BeautifulSoup(html_content, "html.parser")

links = []
for link in soup.find_all('a'):
    href = link.get('href')
    if href:
        links.append(href)

for link in links:
    print(link)
