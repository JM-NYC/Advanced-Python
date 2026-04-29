"""
            This is a change to the file that I will push to github.
            Nothing below has actually changed.
            Last Revised 4/29/2026
"""

import requests
from bs4 import BeautifulSoup

url = 'https://thehardtimes.net/music/metal/slipknot-loses-three-members-due-to-iowa-gerrymandering/'

response = requests.get(url)
contents = response.text
soup = BeautifulSoup(contents, 'html.parser')

title = soup.find("meta", attrs={'property': 'og:title'})
author = soup.find("meta", attrs={'name': 'twitter:data1'})
date = soup.find('time')
readtime = soup.find("meta", attrs={'name': 'twitter:data2'})
maintext = soup.find("div", class_="entry-content")

tt = title.get("content")
at = author.get("content")
dt = date.get_text().strip()
rt = readtime.get("content")
mt = maintext.find_all("p")

print(f'Title: {tt} \n')
print(f'Author: {at} \n')
print(f'Publish Date: {dt} \n')
print(f'Read time: {rt} \n')

for line in mt:
    print(f'{line.text.strip()}\n')
