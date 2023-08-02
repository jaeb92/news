import os
import sys
import yaml
import requests
import argparse
import pandas as pd
sys.path.append('.')

from utils.imgs import save_img
from utils.texts import line_to_space

from bs4 import BeautifulSoup
with open('config/tag.yaml', 'r') as f:
    tag_config = yaml.load(f, Loader=yaml.FullLoader)

with open('config/news_homepage.yaml', 'r') as f:
    site_config = yaml.load(f, Loader=yaml.FullLoader)

news_category = pd.read_excel('data/news_category_eng.xlsx', sheet_name=None, index_col=0)


def get_html(url):
    res = requests.get(url)
    return BeautifulSoup(res.content.decode('utf-8', 'replace'), 'html.parser')

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

    docs = []
    
    for url in detail_urls:
        # print('detail url:', url)
        html = get_html(url)
        try:
            news_id = get_news_id(url)
        except Exception as e:
            print(e)

        try:
            title = line_to_space(html.find(title_tag, title_class).text.strip())
        except Exception as e:
            print(e)

        try:
            if site == 'hankook':
                contents = ' '.join([tag.text for tag in html.find_all('p', 'editor-p')])
                # print(c)
            else:
                contents = line_to_space(html.find(contents_tag, contents_class).text.strip())
        except Exception as e:
            print(e)

        try:
            if site == 'seoul':
                author = contents.split()[0]
            author = line_to_space(html.find(author_tag, author_class).text.strip())
            
        except Exception as e:
            pass
        
        try:
            date = line_to_space(html.find(date_tag, date_class).text.strip())
        except Exception as e:
            print(e)
        # images = html.find_all(image_tag, image_class)
        # images = [tag.find('img').attrs['src'] for tag in images]
        docs.append({
            'news_id': news_id,
            'title': title,
            'contents': contents,
            'author': author,
            'date': date
        })
        # print('news_id:', news_id)
        # print('title:', title)
        # print('contents:', contents[:1000])
        # print("author:", author)
        # print('date:', date)
        # print()
        
    return docs
        # print(images)
        # save_img(images, site, news_id)
        

def get_news_detail_url(url):
    # print('urll:', url)e
    html = get_html(url)
    news_list = html.find(list_tag, list_class)
    # print('news list:',news_list)
    # news_titles = [tag.find_all(list_title_tag, list_title_class) for tag in news_list]
    news_titles = news_list.find_all(list_title_tag, list_title_class)
    # print('news_titles:', news_titles)
    # print(news_titles)
    news_detail_url_tag = [tag.find(detail_tag) for tag in news_titles]
    news_detail_urls = [tag.attrs[detail_attrs] for tag in news_detail_url_tag if tag]
    # print("news_detail_urls:", news_detail_urls)
    if site == 'seoul' or site == 'hani' or site == 'maeil' or site == 'hankook':
        news_detail_urls = [news_main_url + detail_url for detail_url in news_detail_urls]
    # print('news detail urls:',news_detail_urls)
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
    
    news_main_url = site_config['url'][site]['main']
    endpoint = site_config['url'][site]['list_endpoint']
    
    news_list_url = news_main_url + endpoint if endpoint else news_main_url
    # print('news_list_url:', news_list_url)
    
    main_category = site_config['main_category'][0]
    category1 = news_category[main_category][site][0]
    category2 = news_category[main_category][site][1]
    print('category1:', category1, ' category2:', category2)

    if site == 'seoul':
        news_list_url = news_list_url + category2
    elif site == 'khan':
        news_list_url = news_list_url + '/' + category1 + '/' + category2 + '/articles'
    elif site == 'maeil':
        news_list_url = news_list_url + '/' + category2
    else:
        news_list_url = news_list_url + '/' + category1 + '/' + category2
    
    detail_urls = get_news_detail_url(news_list_url)
    # print('detail urls:', detail_urls)
    news = get_news_detail(detail_urls=detail_urls)
    
    print(news)
    print(len(news))