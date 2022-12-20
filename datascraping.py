from bs4 import BeautifulSoup as bs
import requests
import pandas
import secret

player_list = []


# Connects to splash to render website as javascript
def get_soup(url):
    r = requests.get(secret.splash, params= {'url' : url, 'wait' : 2})
    soup = bs(r.text, 'html.parser')
    return soup

def get_reviews(soup):
    players = soup.find_all('div', {'data-hook': 'review'})
    try: 
        for item in players:
            player = {
            'product': soup.title.text.replace('Amazon.co.uk:Customer reviews:', '').strip(),
            'title': item.find('a', {'data-hook': 'review-title'}).text.strip(),
            'rating': float(item.find('i', {'data-hook': 'review-star-rating'}).text.replace('out of 5 stars', '').strip()),
            'body': item.find('span', {'data-hook': 'review-body'}).text.strip(),
            }
            player_list.append(player)
    except:
        pass