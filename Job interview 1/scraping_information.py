import pandas as pd
import requests
from bs4 import BeautifulSoup
from needed_urls import urls
import json

all_data = {}

for url in urls:
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')

    table = soup.find('table')
    if not table:
        continue

    df = pd.read_html(str(table))[0]

    all_data[url] = df.to_dict(orient='records')

with open('scraped_data.json', 'a', encoding='utf-8') as f:
    json.dump(all_data, f, indent=4)