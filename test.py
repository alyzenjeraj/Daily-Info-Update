from bs4 import BeautifulSoup
import requests
from urllib.request import Request, urlopen
import json
import re



def headlinegrabber(response_text):
    soup = BeautifulSoup(response_text, 'lxml')
    headlines = soup.findAll(attrs={"class": "headline"})
    x = 0
    for headline in headlines:
        if 0 < x < 6:
            print(headline.text)
            x = x + 1
        else:
            x = x + 1

    # linksList = []
    # links = soup.find_all('a')
    # for link in soup.findAll('a', attrs={"class": "card cardText relatedCard sclt-contentpackageprimaryrelatedcard1"}):
    #     links.append(link)
    #     print(links)
    
    # print(linksList)


# url = 'https://inshorts.com/en/read'
# response = requests.get(url)
# headlinegrabber(response.text)

# from bs4 import BeautifulSoup
# import requests
# import json


# def headlinegrabber(response_text):
#     soup = BeautifulSoup(response_text, 'lxml')
#     headlines = soup.find_all(attrs={"id": "initialStateDom"})
#     for headline in headlines:
#         print(headline.text)

# from bs4 import BeautifulSoup
# import requests
# import json


# def headlinegrabber(response_text):
#     soup = BeautifulSoup(response_text, 'lxml')
#     headlines = soup.find_all('h3')
#     x=0
#     for headline in headlines:
#         if x < 32:
#             x = x+1  
#         elif 37 > x > 31:
#             x = x + 1
#             print(headline.text)
#             print('')



url = 'https://www.cbc.ca/news'
response = requests.get(url)
headlinegrabber(response.text)