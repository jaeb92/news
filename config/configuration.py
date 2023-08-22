import yaml
import pandas as pd
from typing import Any

class Config:
    def __init__(self, site, category):
        
        with open('config/category.yaml', 'r') as f:
            categories = yaml.load(f, Loader=yaml.FullLoader)
            self.category = categories[site][category]
            self.main_category = list(self.category.keys())[0]
            self.sub_categories = self.category[self.main_category]
        
        with open('config/url.yaml', 'r') as f:
            url = yaml.load(f, Loader=yaml.FullLoader)
            self.url = url[site]
            self.urls = {
                'main': self.url['main'],
                'endpoint': self.url['list_page_endpoint']
            }
            
            
        with open('config/tag.yaml', 'r') as f:
            tag = yaml.load(f, Loader=yaml.FullLoader)
            self.tag = tag[site]
            
            # self.list_tag = self.tag['list']['tag']
            # self.list_class = self.tag['list']['class']
            
            # self.list_title_tag = self.tag['list_title']['tag']
            # self.list_title_class = self.tag['list_title']['class']

            # self.detail_tag = self.tag['detail_url']['tag']
            # self.detail_attrs = self.tag['detail_url']['attrs']

            # self.title_tag = self.tag['title']['tag']
            # self.title_class = self.tag['title']['class']

            # self.contents_tag = self.tag['contents']['tag']
            # self.contents_class = self.tag['contents']['class']

            # self.author_tag = self.tag['author']['tag']
            # self.author_class = self.tag['author']['class']
            
            # self.date_tag = self.tag['date']['tag']
            # self.date_class = self.tag['date']['class']
            
            # self.image_tag = self.tag['image']['tag']
            # self.image_class = self.tag['image']['class']
            
            # self.news_main_url = self.url['main']
            # self.endpoint = self.url['list_page_endpoint']
            
            self.tags = {
                'list_tag': self.tag['list']['tag'],
                'list_class': self.tag['list']['class'],
                'list_title_tag': self.tag['list_title']['tag'],
                'list_title_class': self.tag['list_title']['class'],
                'detail_url_tag': self.tag['detail_url']['tag'],
                'detail_url_attrs': self.tag['detail_url']['attrs'],
                'title_tag': self.tag['title']['tag'],
                'title_class': self.tag['title']['class'],
                'contents_tag': self.tag['contents']['tag'],
                'contents_class': self.tag['contents']['class'],
                'author_tag': self.tag['author']['tag'],
                'author_class': self.tag['author']['class'],
                'date_tag': self.tag['date']['tag'],
                'date_class': self.tag['date']['class'],
                'image_tag': self.tag['image']['tag'],
                'image_class': self.tag['image']['class']   
            }
            
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        return self.main_category, self.sub_categories, self.urls, self.tags
        
        tag = tag[self.site]
        
        self.list_tag = tag['list']['tag']
        self.list_class = tag['list']['class']
        
        self.list_title_tag = tag['list_title']['tag']
        self.list_title_class = tag['list_title']['class']

        self.detail_tag = tag['detail_url']['tag']
        self.detail_attrs = tag['detail_url']['attrs']

        self.title_tag = tag[site]['title']['tag']
        self.title_class = tag[site]['title']['class']

        self.contents_tag = tag[site]['contents']['tag']
        self.contents_class = tag[site]['contents']['class']

        self.author_tag = tag[site]['author']['tag']
        self.author_class = tag[site]['author']['class']
        
        self.date_tag = tag[site]['date']['tag']
        self.date_class = tag[site]['date']['class']
        
        self.image_tag = tag[site]['image']['tag']
        self.image_class = tag[site]['image']['class']
        
        self.news_main_url = site_config['url'][self.site]['main']
        self.endpoint = site_config['url'][self.site]['list_endpoint']