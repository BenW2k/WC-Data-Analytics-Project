from bs4 import BeautifulSoup as bs
import requests
import pandas
import secret

# Connects to splash to render website as javascript
def get_soup(url):
    r = requests.get(secret.splash, params= {'url' : url, 'wait' : 2})
    soup = bs(r.text, 'html.parser')
    return soup


 