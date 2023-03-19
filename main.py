import requests
from bs4 import BeautifulSoup

URL = "https://coinmarketcap.com/"

res = requests.get(URL)

if res.status_code == 200:
  soup = BeautifulSoup(res.text, feature="html.parser")
  info = soup.find_all("a", {"href":"/currencies/bitcoin/markets/"})
  print(info[0])