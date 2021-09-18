import requests
from bs4 import BeautifulSoup

URL = 'http://api.scraperapi.com/?api_key=c59648ab998ca23833e502f4638bfc49&url=https://www.grubhub.com/food/the_ice_cream_shop&render=true&country_code=us'
page = requests.get(URL)

with open("aaa.html", "w") as f:
    f.write(page.text)

soup = BeautifulSoup(page.content, 'html.parser')

all_s_row_elems = soup.find_all('div', class_='s-row', recursive=True)

print(len(all_s_row_elems))
state_elems = all_s_row_elems[10:77]

print(len(state_elems))
for i, state_elem in enumerate(state_elems):
    if i == 0:
        city_elems = soup.find_all('a', recursive=True)
        for j, city_elem in enumerate(city_elems):
            if j == 0:
                print(city_elem)
