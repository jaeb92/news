import json
import yaml
import requests
from bs4 import BeautifulSoup

with open('config/config.yaml', 'r') as f:
    url = yaml.load(f, Loader=yaml.FullLoader)['url']

category = {}
try:
    res = requests.get(url)
    text = res.text
except:
    text = None

soup = BeautifulSoup(text, 'html.parser')
c = soup.find_all("dl", "list01")
hrefs = list(map(lambda x: x.attrs['href'].replace('//', ''), c[0].find_all('a')))
category_name = list(map(lambda x: x.split('/')[1] if len(x.split('/')) > 0 else x, hrefs))
category_name = list(filter(lambda x: x, category_name))
category_name.insert(0, 'main')
print(category_name)
for c_name, c_href in zip(category_name, hrefs):
    category[c_name] = {}
    category[c_name]['href'] = c_href

with open('config/category.json', 'w') as f:
    json.dump(category, f, ensure_ascii=False)