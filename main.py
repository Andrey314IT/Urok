import requests
from bs4 import BeautifulSoup

URL = "https://coinmarketcap.com/"

res = requests.get(URL)
