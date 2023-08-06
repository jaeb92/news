import json
import argparse
import traceback

# get raw contents from news homepage
from crawling.crawling import NewsCrawler

# preprocess for contents
from preprocess import *

# save to elasticsearch index
from elastic.es import ElasticSearch

# python kafka client
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers=['kafka-1:9092', 'kafka-2:9092', 'kafka-3:9092'],
    client_id='news_raw_producer',
    key_serializer=None,
    value_serializer=lambda x: json.dumps(x).encode("utf-8")
)

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--site', dest='site', help='ex. chosun, joonang, donga, seoul, khan, maeil, hani, hankook')
    args = parser.parse_args()
    site = args.site
    print(f"Start python kafka stream pipeline for \'{site}\'")

    newsCrawler = NewsCrawler(site)
    news_list_url = newsCrawler.get_news_list_url()
    news_detail_urls = newsCrawler.get_news_detail_url(news_list_url=news_list_url)
    news_docs = newsCrawler.get_news_detail(news_detail_urls)
    
    es = ElasticSearch()
    try:
        for doc in news_docs:
            res = es.insert(index='news', document=doc)
            print("res:", res)
    except:
        traceback.print_exc()   
