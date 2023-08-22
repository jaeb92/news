from abc import ABC, abstractmethod
from crawling.crawler import Crawler, Hankook, Donga, Joongang

class CrawlerCreator(ABC):
    @abstractmethod
    def create(self):
        pass
    
    def crawl(self):
        crawler = self.create()
        res = crawler.crawl()
        return res
        
        
class HankookCreator(CrawlerCreator):
    def __init__(self, config):
        self.config = config
        pass
    
    def create(self) -> Crawler:
        return Hankook(self.config)
    
    
class JoongangCreator(CrawlerCreator):
    
    def __init__(self, config):
        self.config = config
        pass
    
    def create(self) -> Crawler:
        return Joongang(self.config)
    
    
class DongaCreator(CrawlerCreator):
    def __init__(self, config):
        self.config = config
        pass
    
    def create(self) -> Crawler:
        return Donga(self.config)