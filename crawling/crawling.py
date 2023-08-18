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

with open('config/news_info.yaml', 'r') as f:
    site_config = yaml.load(f, Loader=yaml.FullLoader)

news_category = pd.read_excel('data/news_category_eng.xlsx', sheet_name=None, index_col=0)


class NewsCrawler:
    def __init__(self, site):
        self.site = site
        news_tag = tag_config[self.site]
        
        self.list_tag = news_tag['list']['tag']
        self.list_class = news_tag['list']['class']
        
        self.list_title_tag = news_tag['list_title']['tag']
        self.list_title_class = news_tag['list_title']['class']

        self.detail_tag = news_tag['detail_url']['tag']
        self.detail_attrs = news_tag['detail_url']['attrs']

        self.title_tag = tag_config[site]['title']['tag']
        self.title_class = tag_config[site]['title']['class']

        self.contents_tag = tag_config[site]['contents']['tag']
        self.contents_class = tag_config[site]['contents']['class']

        self.author_tag = tag_config[site]['author']['tag']
        self.author_class = tag_config[site]['author']['class']
        
        self.date_tag = tag_config[site]['date']['tag']
        self.date_class = tag_config[site]['date']['class']
        
        self.image_tag = tag_config[site]['image']['tag']
        self.image_class = tag_config[site]['image']['class']
        
        self.news_main_url = site_config['url'][self.site]['main']
        self.endpoint = site_config['url'][self.site]['list_endpoint']
        

    def get_html(self, url: str) -> BeautifulSoup:
        """_summary_

        Args:
            url (str): url of homepage for crawling

        Returns:
            BeautifulSoup: result of crawling (html)
        """
        res = requests.get(url)
        return BeautifulSoup(res.content.decode('utf-8', 'replace'), 'html.parser')


    def get_news_id(self, news_detail_url: str) -> str:
        """
        
        return news id

        Args:
            news_detail_url (str): news detail page url

        Returns:
            str: news id
        """
        if self.site == 'donga':
            news_id = news_detail_url.split('/')[-2]
        elif self.site == 'hani':
            news_id = news_detail_url.split('/')[-1].split('.')[0]
        elif self.site == 'seoul':
            news_id = news_detail_url.split('id=')[-1]
        else:
            news_id = news_detail_url.split('/')[-1]

        return str(news_id)


    def get_news_detail(self, detail_urls: list) -> list:
        """
        get news main contents (title, contents, author, date, news id and images)

        Args:
            detail_urls (list): news detail page urls

        Returns:
            list: news main contents
        """
        news_id = ""
        title = ""
        contents = ""
        author = ""
        date = ""
        images = ""
        source = self.site

        docs = []
                
        for url in detail_urls:
            html = self.get_html(url)
            try:
                news_id = self.get_news_id(url)
            except Exception as e:
                print(e)

            try:
                title = line_to_space(html.find(self.title_tag, self.title_class).text)
            except Exception as e:
                print(e)

            try:
                if self.site == 'hankook':
                    contents = ' '.join([tag.text for tag in html.find_all('p', 'editor-p')])
                else:
                    contents = line_to_space(html.find(self.contents_tag, self.contents_class).text)
            except Exception as e:
                print(e)

            try:
                if self.site == 'seoul':
                    author = contents.split()[0]
                author = line_to_space(html.find(self.author_tag, self.author_class).text)
                
            except Exception as e:
                pass
            
            try:
                date = line_to_space(html.find(self.date_tag, self.date_class).text)
            except Exception as e:
                print(e)

            # images = html.find_all(image_tag, image_class)
            # images = [tag.find('img').attrs['src'] for tag in images]
            docs.append({
                'news_id': news_id.strip(),
                'title': title.strip(),
                'contents': contents.strip(),
                'author': author.strip(),
                'date': date.strip(),
                'source': source.strip()
            })
    
        return docs
    

    def get_news_detail_url(self, news_list_url: str) -> list:
        """
        get news detail page urls

        Args:
            url (str): news list page url

        Returns:
            list: news detail page urls
        """

        html = self.get_html(news_list_url)
        news_list = html.find(self.list_tag, self.list_class)
        news_titles = news_list.find_all(self.list_title_tag, self.list_title_class)
        news_detail_url_tag = [tag.find(self.detail_tag) for tag in news_titles]
        news_detail_urls = [tag.attrs[self.detail_attrs] for tag in news_detail_url_tag if tag]

        if self.site == 'seoul' or self.site == 'hani' or self.site == 'maeil' or self.site == 'hankook':
            news_detail_urls = [self.news_main_url + detail_url for detail_url in news_detail_urls]

        return news_detail_urls


    def get_news_list_url(self) -> str:
        """
        return news list page url

        Returns:
            str: news list page url 
        """
        news_list_url = self.news_main_url + self.endpoint if self.endpoint else self.news_main_url
        # print('news_list_url:', news_list_url)
        
        main_category = site_config['main_category'][0]
        category1 = news_category[main_category][self.site][0]
        category2 = news_category[main_category][self.site][1]
        print('category1:', category1, ' category2:', category2)

        if self.site == 'seoul':
            news_list_url = news_list_url + category2
        elif self.site == 'khan':
            news_list_url = news_list_url + '/' + category1 + '/' + category2 + '/articles'
        elif self.site == 'maeil':
            news_list_url = news_list_url + '/' + category2
        else:
            news_list_url = news_list_url + '/' + category1 + '/' + category2
    
        return news_list_url
    

if __name__ == '__main__':

    newsCrawler = NewsCrawler('joongang')
    news_list_url = newsCrawler.get_news_list_url()
    news_detail_urls = newsCrawler.get_news_detail_url(news_list_url)
    news_details = newsCrawler.get_news_detail(news_detail_urls)

    print(len(news_details))