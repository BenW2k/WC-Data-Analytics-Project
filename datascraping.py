from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import secret

player_list = []


# Connects to splash to render website as javascript
def get_soup(url):
    r = requests.get(secret.splash, params= {'url' : url, 'wait' : 2})
    soup = bs(r.text, 'html.parser')
    return soup

def get_summary_player_data(soup):
# Used to get the data from the first set of data: the summary tab
    players = soup.find_all('div', {'id': 'statistics-table-summary'})
    try: 
        for data in players:
            player = {
            'name': data.find('span', {'class': 'iconize iconize-icon-left'}).text.strip(),
            'nationality': data.find('span', {'class': 'team-name'}).text.strip(),
            'goals': int(data.find('td', {'class': 'goal'}).strip()),
            'yellow cards': data.find('td', {'class': 'yellowCard'}).text.strip(),
            'red cards': data.find('td', {'class': 'redCard'}).text.strip(),
            'shots per game': float(data.find('td', {'class': 'shotsPerGame'}).text.split()),
            'passing%': float(data.find('td', {'class': 'passSuccess'}).text.split()),
            'aerials won': float(data.find('td', {'class': 'aerialWonPerGame'}).text.split()),
            'MotM awards': int(data.find('td', {'class': 'manOfTheMatch'}).text.split())
            }
            player_list.append(player)
    except:
        pass
