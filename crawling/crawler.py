import requests
import pprint
from bs4 import BeautifulSoup
from abc import ABC, abstractmethod

class Crawler(ABC):
    def __init__(self, config) -> None:
        self.main_category, self.sub_categories, self.urls, self.tags = config()
        self.base_url = self.urls['base']
        self.endpoint = self.urls['endpoint']
        
    @abstractmethod
    def crawl(self):
        """
        interface abstract method
        """
        pass
    
    def get_html(self, url):
        res = requests.get(url)
        return BeautifulSoup(res.content.decode('utf-8', 'replace'), 'html.parser')
    
    @abstractmethod
    def get_sub_category_url(self):
        pass
    
    @abstractmethod
    def get_detail_url(self):
        pass
    
    @abstractmethod
    def get_news_detail(self):
        pass
    
    
class Hankook(Crawler):
    def __init__(self, config) -> None:
        super().__init__(config)
        
        
    def get_sub_category_url(self) -> list:
        """
        하위 카테고리의 url을 생성하여 반환    

        Returns:
            list: 뉴스 하위 카테고리 url 리스트
        """
        news_list_urls = []
        for sub_category in self.sub_categories:
            news_list_url = self.base_url + self.endpoint if self.endpoint else self.base_url
            url = news_list_url + '/' + self.main_category + '/' + sub_category
            news_list_urls.append(url)

        return news_list_urls
        
    def get_detail_url(self, news_list_url: str) -> list:
        """
        뉴스 상세페이지의 url을 추출

        Args:
            news_list_url (str): 뉴스목록 url

        Returns:
            list: 뉴스상세페이지 url이 담긴 리스트
        """
        news_list_html = self.get_html(news_list_url)
        news_list = news_list_html.find(self.tags['list_tag'], self.tags['list_class'])
        news_titles = news_list.find_all(self.tags['list_title_tag'], self.tags['list_title_class'])
        news_detail_url_tags = [tag.find(self.tags['detail_url_tag']) for tag in news_titles]
        news_detail_urls = [tag.attrs[self.tags['detail_url_attrs']] for tag in news_detail_url_tags if tag]
        news_detail_urls = [self.base_url + detail_url for detail_url in news_detail_urls]

        return news_detail_urls

    def get_news_detail(self, detail_url: str) -> list:
        """
        뉴스 상세 내용 추출 (news_id, title, contents, author, date, source(출처))

        Args:
            detail_url (str): 상세페이지 url

        Returns:
            list: 뉴스 상세 내용
        """
        docs = []
        
        detail_html = self.get_html(detail_url)
        news_id = detail_url.split('/')[-1]
        title = detail_html.find(self.tags['title_tag'], self.tags['title_class'])
        contents = detail_html.find(self.tags['contents_tag'], self.tags['contents_class'])
        author = detail_html.find(self.tags['author_tag'], self.tags['author_class'])
        date = detail_html.find(self.tags['date_tag'], self.tags['date_class'])
        
        docs = {
            'news_id': news_id.strip() if news_id else '',
            'title': title.text.strip() if title else '',
            'contents': contents.text.strip() if contents else '',
            'author': author.text.strip() if author else '',
            'date': date.text.strip() if date else '',
            'source': 'hankook'
        }
        
        return docs        
        
        
    def crawl(self):
        """
        hankookilbo crawl service code
        """
        sub_category_urls = self.get_sub_category_url()
        news_list = []
        
        for url in sub_category_urls:
            news_detail_urls = self.get_detail_url(url)
            for detail_url in news_detail_urls:
                news = self.get_news_detail(detail_url)
                news_list.append(news)
            
        return news_list


class Joongang(Crawler):
    def __init__(self, config) -> None:
        super().__init__(config)
    
    def get_detail_url(self):
        """
        do something
        """
        return ""
    
    def get_sub_category_url(self):
        """
        do something
        """
        return ""
    
    def get_news_detail(self):
        """
        do something
        """
        return ""

    def crawl(self):
        """
        joongangilbo crawl service code
        """
        pass
    
    
class Donga(Crawler):
    def __init__(self, config) -> None:
        super().__init__(config)
        
    def get_detail_url(self):
        """
        do something
        """
        return ""
    
    def get_sub_category_url(self):
        """
        do something
        """
        return ""
    
    def get_news_detail(self):
        """
        do something
        """
        return ""
    
    def crawl(self):
        """
        Dongailbo crawl service code
        """
        pass
    