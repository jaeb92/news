import argparse

from config.configuration import Config
from crawling.creator import *

def main(crawler: Crawler):
    res = crawler.crawl()
    print(len(res))
    # print('crawling result:', res)
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--site', dest='site', help='ex. chosun, joonang, donga, seoul, khan, maeil, hani, hankook')
    parser.add_argument('-c', '--category', dest='category', help='ex. politics, economy, international, society, culture, entertinament, sports')
    args = parser.parse_args()

    site = args.site
    category = args.category
    
    config = Config(site, category)

    if site == 'hankook':
        main(HankookCreator(config))
        
    elif site == 'joongang':
        main(JoongangCreator(config))
        
    elif site == 'donga':
        main(DongaCreator(config))
