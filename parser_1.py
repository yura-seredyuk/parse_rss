"""
'pravda.com.ua' parser
"""
from bs4 import BeautifulSoup
import requests
from pprint import pprint


def parse(url):

    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'lxml')

    article = soup.find('article', class_='post')
    
    # print(article)

    data = {}
    if article.find('img', class_='post_photo_news_img'):
        data['preview'] = article.find('img', class_='post_photo_news_img').get('src')
    # print(data['preview'])
    post_text = article.find('div', class_='post_text')

    data['content'] = []
    element = post_text.find('p')
    data['content'].append({'p':element.text})
    while element != None:
       element = element.find_next_sibling()
       if element == None: break
       if element.name == 'p':
           data['content'].append({'p':element.text})
    #    elif element.name == 'div' :
    #     #    print(element)
    #        img = element.find('img')
    #        if img == None: continue
    #        data['content'].append({'img':'https:'+img.get('src')})
    
    # pprint(data['content']) 
    return data

  


if __name__ == '__main__':
    
    parse('https://www.pravda.com.ua/news/2021/06/24/7298338/')