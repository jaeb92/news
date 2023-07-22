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


def get_news_contents(category):
    category_depth = category_config[category]['depth']
    print(category_depth)
    url = main_url + f'/{category}/' + 'baseball'
    # for i, c in enumerate(category_depth):
    #     url = main_url + f'/{category}/'
    #     url += c
    #     print(i+1, c, url)
    # print('url:', url)
    html = requests.get(url)
    contents = BeautifulSoup(html.text, 'html.parser')
    news_list = contents.find_all("section", "box-type box-latest01") 
    news_title_tags = news_list[0].find_all("strong", "tit-news")
    news_contents_lead_tags = news_list[0].find_all('p', 'lead')
    news_detail_urls_tags = news_list[0].find_all('a', 'tit-wrap')
    news_detail_urls = [tag.attrs['href'] for tag in news_detail_urls_tags]
    news_detail_urls = list(map(lambda x: x.replace('//', 'https://'), news_detail_urls))
    news_titles = [tag.text for tag in news_title_tags]
    news_lead_contents = [tag.text for tag in news_contents_lead_tags]
    # print(news_titles)
    # print(news_detail_urls)
    article = {'news': []}
    for i, (title, lead, url) in enumerate(zip(news_titles, news_lead_contents, news_detail_urls)):
    #     # print(i, title, lead)
        # print(f'링크{i+1}:',url)
        html_detail_news = requests.get(url)
        news_detail = BeautifulSoup(html_detail_news.text, 'html.parser')
        news_guid = url.split('view/')[-1].split('?')[0]
        # print(news_guid)
        news_reporter = [reporter.text.split(' ')[0] for reporter in news_detail.find_all('strong', 'tit-name')]
        news_title = news_detail.find('h1', 'tit').text
        news_update_time = news_detail.find("p", "update-time").text.replace('송고시간', '').strip()
        news_contents = news_detail.find('article', 'story-news article').find_all('p')
        news_contents = ' '.join([contents.text for contents in news_contents])
        news_contents = news_contents.replace('\n', ' ')
        # print("=====================================================")
        # print('id:', news_guid)
        # print('title:', news_title)
        # print('contents:', news_contents[:])
        # print('time:', news_update_time.strip())
        # print("reporter:", news_reporter)
        # print("=====================================================")

        article['news'].append({news_guid: {'title': news_title, 'contents': news_contents, 'news_dt': news_update_time, 'reporter': news_reporter}})
        print(article['news'])
        # return

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--category', dest='category', help=', '.join(category_name))
    # parser.add_argument('--depth', dest='depth', help='\'all\', or specific category')

    args = parser.parse_args()
    category = args.category
    # depth = args.depth 
    contents = get_news_contents(category=category)
    # print(contents)
# urls = [category_config[c]['href'] for c in category]
# html = requests.get(urls[-3])

# def get_all_news(url):
#     html = requests.get(url)
#     return html.text


# if __name__ == '__main__': 
#     url = urls[-3]
#     url = url.split('/', 2)
#     print(url)
    # news = get_all_news(url)
    # print(news)
    # print('url:', url)