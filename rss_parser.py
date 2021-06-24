from os import link
from feedparser import * 
from pprint import pprint
from datetime import datetime
from time import mktime

import parser_1


RSS_URL = 'https://www.pravda.com.ua/rss/view_news/'

feed = parse(RSS_URL)
# pprint(feed)

urls = [
    'pravda.com.ua',
    'eurointegration.com.ua',
    'life.pravda.com.ua',
    'epravda.com.ua'
]

news = []

for item in feed.entries:
    data = {}
    data['title'] = item.title
    data['description'] = item.summary
    data['url'] = item.link
    data['date'] = datetime.fromtimestamp(mktime(item.published_parsed))
    

    if data['url'].split('/')[2][4:] == 'pravda.com.ua':
        data['content'] = parser_1.parse(data['url'])
        
    news.append(data)

pprint(news)

