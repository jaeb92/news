import os
import sys

import sys
sys.path.append('/Users/jaeb/news/utils')
print(sys.path)
import yaml
import requests
import argparse
import pandas as pd

from utils.imgs import save_img
from bs4 import BeautifulSoup
with open('config/tag.yaml', 'r') as f:
    tag_config = yaml.load(f, Loader=yaml.FullLoader)

with open('config/news_homepage.yaml', 'r') as f:
    site_config = yaml.load(f, Loader=yaml.FullLoader)

news_category = pd.read_excel('data/news_category_eng.xlsx', sheet_name=None, index_col=0)


def test_get_html(url):
    res = requests.get(url)
    return BeautifulSoup(res.text, 'html.parser')

def get_news_id(url):
    if site == 'donga':
        news_id = url.split('/')[-2]
    elif site == 'hani':
        news_id = url.split('/')[-1].split('.')[0]
    elif site == 'seoul':
        news_id = url.split('id=')[-1]
    else:
        news_id = url.split('/')[-1]

    return str(news_id)


def get_news_detail(detail_urls):
    news_id = ""
    title = ""
    contents = ""
    author = ""
    date = ""
    images = ""

    for url in detail_urls:
        html = get_html(url)
        news_id = get_news_id(url)
        title = html.find(title_tag, title_class).text
        contents = html.find(contents_tag, contents_class).text
        author = html.find(author_tag, author_class).text
        date = html.find(date_tag, date_class).text
        images = html.find_all(image_tag, image_class)
        images = [tag.find('img').attrs['src'] for tag in images]
        print('news_id:', news_id)
        print('title:', title)
        print('contents:', contents[:100])
        print("author:", author)
        print('date:', date)
        print(images)
        save_img(images, site, news_id)
        

def get_news_detail_url(url):
    html = get_html(url)
    news_list = html.find_all(list_tag, list_class)
    news_titles = [tag.find(list_title_tag, list_title_class) for tag in news_list]
    news_detail_url_tag = [tag.find(detail_tag) for tag in news_titles]
    news_detail_urls = [tag.attrs[detail_attrs] for tag in news_detail_url_tag if tag]
    return news_detail_urls


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--site', dest='site', help='ex. chosun, joonang, donga, seoul, khan, maeil, hani, hankook')
    args = parser.parse_args()
    site = args.site
    print("site:", site)
    news_tag = tag_config[site]
    
    list_tag = news_tag['list']['tag']
    list_class = news_tag['list']['class']
    
    list_title_tag = news_tag['list_title']['tag']
    list_title_class = news_tag['list_title']['class']

    detail_tag = news_tag['detail_url']['tag']
    detail_attrs = news_tag['detail_url']['attrs']

    title_tag = tag_config[site]['title']['tag']
    title_class = tag_config[site]['title']['class']

    contents_tag = tag_config[site]['contents']['tag']
    contents_class = tag_config[site]['contents']['class']

    author_tag = tag_config[site]['author']['tag']
    author_class = tag_config[site]['author']['class']
    
    date_tag = tag_config[site]['date']['tag']
    date_class = tag_config[site]['date']['class']
    
    image_tag = tag_config[site]['image']['tag']
    image_class = tag_config[site]['image']['class']
    
    news_base_url = site_config['news_url'][site]
    main_category = site_config['main_category'][0]
    category1 = news_category[main_category][site][0]
    category2 = news_category[main_category][site][2]
    url = news_base_url + '/' + category1 + '/' + category2
    detail_urls = get_news_detail_url(url)
    get_news_detail(detail_urls=detail_urls)