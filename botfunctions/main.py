import requests
import json
from newsgrabber import headlinegrabber


url = 'https://www.cbc.ca/news'
response = requests.get(url)
headlinegrabber(response.text)




