import json
import argparse
import traceback

# db module
from db.dbconn import Database

# get raw contents from news homepage
from crawling.crawling import NewsCrawler

# preprocess for contents
from preprocess import *

from config.configuration import Config

# save to elasticsearch index
# from elastic.es import ElasticSearch

def save(docs: list):
    table = 'news'
    columns = db.get_table_column_name(table=table)
    columns = ','.join(columns)
    sql = f"insert into {table} ({columns}) values %s"
    values = [tuple(doc.values()) for doc in news_docs]

    # print(values)
    db.insert_bulk(q=sql, arg=values)



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--site', dest='site', help='ex. chosun, joonang, donga, seoul, khan, maeil, hani, hankook')
    args = parser.parse_args()
    site = args.site
    
    config = Config(site)
    news_info, tag = config.get_config()
    print(f"Start python kafka stream pipeline for \'{site}\'")

    
    newsCrawler = NewsCrawler(site)
    news_list_url = newsCrawler.get_news_list_url()
    news_detail_urls = newsCrawler.get_news_detail_url(news_list_url=news_list_url)
    news_docs = newsCrawler.get_news_detail(news_detail_urls)
    
    db = Database()
    save(news_docs)