import time
import yaml
import aiohttp
import aiofiles
import asyncio
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from db.dbconn import Database

today = datetime.today()
today = datetime.strftime(today, '%Y%m%d')

main_url = 'https://hankookilbo.com'
main_category = "Politics"
subcategories = ["HA01","HA02","HA03","HA04","HA99"]
db_columns = ['title', 'contents', 'author', 'date', 'source']
columns = ','.join(db_columns)
table = 'news'
baseurl = main_url + '/News/{category}/{subcategory}?SortType=&SearchDate={today}'

db = Database()
async def save(news):
    sql = f"insert into {table} ({columns}) values %s"
    values = [tuple(n.values()) for n in news]
    db.insert_bulk(q=sql, arg=values)
    
    
async def get_html(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers={'User-Agent':'Mozilla/5.0'}) as resp:
            html_text = await resp.text()
            html = BeautifulSoup(html_text, 'html.parser')
            return html
        
        
async def get_detail_url(html):
    list_tag = 'ul'
    list_class = 'board-list column-3'
    news_list = html.find(list_tag, list_class)
    
    list_title_tag = 'h3'
    list_title_class = ''
    
    news_titles = news_list.find_all(list_title_tag, list_title_class)
    
    detail_url_tag = 'a'
    detail_url_tags = [tag.find(detail_url_tag) for tag in news_titles]

    detail_urls = [tag.attrs['href'] for tag in detail_url_tags if tag]
    detail_urls = [main_url + detail_url for detail_url in detail_urls]

    return detail_urls
    
    
async def get_news(url: str):
    title = ''
    author = ''
    date = ''
    contents = ''
    source = 'hankook'
    
    news_list_html = await get_html(url)
    news_detail_urls = await get_detail_url(news_list_html)
    detail_html = (await get_html(url) for url in news_detail_urls)

    news = []
    
    async for html in detail_html:
        title = html.find('h2', 'title').text
        author = html.find('span', 'nm').text
        date = html.find('dl', 'wrt-text').text
        contents = ' '.join([tag.text for tag in html.find_all('p', 'editor-p')])
        
        news.append({
            'title': title.strip(),
            'author': author.strip(),
            'date': date.strip(),
            'contents': contents.strip(),
            'site': source
        })
        
    await save(news)
    
    
async def run():
    futures = [asyncio.ensure_future(get_news(baseurl.format(category=main_category, subcategory=subcategory, today=today))) for subcategory in subcategories]
    await asyncio.gather(*futures)

    
if __name__ == '__main__':
    # start time
    start = time.time()
    
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())
    loop.close()
    
    # end time
    end = time.time()
    print(f"running time: {end - start:.4f}s")