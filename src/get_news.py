import json
import yaml
import uuid
import requests
import argparse
from bs4 import BeautifulSoup

with open("config/category.json", "r") as f:
    category_config = json.load(f)
with open("config/config.yaml", "r") as f:
    main_url = yaml.load(f, Loader=yaml.FullLoader)['url']

category_name = list(category_config.keys())


class News:
    def __init__(self, category):
        self.main_url = main_url + f'/{category}/' + 'baseball'

    def get_news_main_html(self):
        html = requests.get(self.main_url)
        self.contents = BeautifulSoup(html.text, 'html.parser')

    def get_total_news_page_count(self):
        """
        기사의 전체 페이지 번호가 담긴 리스트를 반환

        Returns:
            list: 기사의 페이지 번호가 담긴 리스트
        """
        paging = self.contents.find_all('div', 'paging paging-type01')
        page_num = paging[0].find_all('a', 'num')
        page_num = [int(page.text) for page in page_num]
        page_num.insert(0,1)
        page_num = list(set(page_num))
        return page_num

    def get_news_list(self):
        """
        기사 리스트 html 태그를 반환

        Returns:
            bs4.element.Tag: 
        """
        news_list_tags = self.contents.find("section", "box-type box-latest01")
        return news_list_tags
    
    def get_news_titles(self):
        """
        기사의 제목 리스트를 반환

        Returns:
            list: 기사제목의 리스트
        """
        news_title_tags =self.get_news_list().find_all("strong", "tit-news")
        news_titles = [tag.text for tag in news_title_tags]
        return news_titles

    def get_news_leads(self):
        """
        기사내용의 미리보기 내용을 반환

        Returns:
            list: 기사의 미리보기 내용의 리스트
        """
        news_contents_lead_tags = self.get_news_list().find_all('p', 'lead')
        news_contents_leads = [tag.text.replace('\n', '') for tag in news_contents_lead_tags]
        return news_contents_leads

    def get_news_detail_url(self):
        news_detail_urls_tags = self.get_news_list().find_all('a', 'tit-wrap')
        news_detail_urls = [tag.attrs['href'] for tag in news_detail_urls_tags]
        news_detail_urls = list(map(lambda x: x.replace('//', 'https://'), news_detail_urls))
        print(news_detail_urls)

    def get_news_detail(self):
        pass


news = News('sports')
news_title_list = news.get_news_titles()
news_leads_list = news.get_news_leads()
news_detail_url = news.get_news_detail_url()
# print(news_title_list)
# print()



# def get_total_news_page_count(url) -> list:
#     html = requests.get(url)
#     contents = BeautifulSoup(html.text, 'html.parser')
#     paging = contents.find_all('div', 'paging paging-type01')
#     page_num = paging[0].find_all('a', 'num')
#     page_num = [int(page.text) for page in page_num]
#     page_num.insert(0,1)
#     page_num = list(set(page_num))
    
#     return page_num

# def get_news_contents(category):
#     category_depth = category_config[category]['depth']
#     # check total page count
#     print(category_depth)
#     url = main_url + f'/{category}/' + 'baseball'
#     # for i, c in enumerate(category_depth):
#     #     url = main_url + f'/{category}/'
#     #     url += c
#     #     print(i+1, c, url)
#     # print('url:', url)
#     html = requests.get(url)
#     contents = BeautifulSoup(html.text, 'html.parser')
#     news_list = contents.find_all("section", "box-type box-latest01") 
#     news_title_tags = news_list[0].find_all("strong", "tit-news")
#     news_contents_lead_tags = news_list[0].find_all('p', 'lead')
#     news_detail_urls_tags = news_list[0].find_all('a', 'tit-wrap')
#     news_detail_urls = [tag.attrs['href'] for tag in news_detail_urls_tags]
#     news_detail_urls = list(map(lambda x: x.replace('//', 'https://'), news_detail_urls))
#     news_titles = [tag.text for tag in news_title_tags]
#     news_lead_contents = [tag.text for tag in news_contents_lead_tags]
#     paging = contents.find_all('div', 'paging paging-type01')
#     page_num = paging[0].find_all('a', 'num')
#     page_num = [int(page.text) for page in page_num]
#     page_num.insert(0,1)
#     page_num = list(set(page_num))
#     # paging = [page.text for page in paging]
    
#     ############ 다음 10개 페이지 ############
#     # for page in paging:
#     #     if page.find('a', 'next'):
#     #         print(page)
#     ########################################
#     print()
#     article = {'news': []}
#     for page in page_num:

#         for i, (title, lead, url) in enumerate(zip(news_titles, news_lead_contents, news_detail_urls)):
#         #     # print(i, title, lead)
#             return
#             html_detail_news = requests.get(url)
#             news_detail = BeautifulSoup(html_detail_news.text, 'html.parser')
#             news_guid = url.split('view/')[-1].split('?')[0]
#             # print(news_guid)
#             news_reporter = [reporter.text.split(' ')[0] for reporter in news_detail.find_all('strong', 'tit-name')]
#             news_title = news_detail.find('h1', 'tit').text
#             news_update_time = news_detail.find("p", "update-time").text.replace('송고시간', '').strip()
#             news_contents = news_detail.find('article', 'story-news article').find_all('p')
#             news_contents = ' '.join([contents.text for contents in news_contents])
#             news_contents = news_contents.replace('\n', ' ')
#             # print(news_detail)
#             return
#             # article['news'].append({news_guid: {'title': news_title, 'contents': news_contents, 'news_dt': news_update_time, 'reporter': news_reporter}})
#     return article
# if __name__ == '__main__':
#     parser = argparse.ArgumentParser()
#     parser.add_argument('--category', dest='category', help=', '.join(category_name))
#     # parser.add_argument('--depth', dest='depth', help='\'all\', or specific category')

#     args = parser.parse_args()
#     category = args.category
#     article = get_news_contents(category=category)
#     print(len(article['news']))