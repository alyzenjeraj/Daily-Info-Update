# from bs4 import BeautifulSoup
# import requests
# import json


# def headlinegrabber(response_text):
#     soup = BeautifulSoup(response_text, 'lxml')
#     headlines = soup.find_all(attrs={"itemprop": "headline"})
    # for headline in headlines:
    #     print(headline.text)


# url = 'https://inshorts.com/en/read'
# response = requests.get(url)
# headlinegrabber(response.text)

from bs4 import BeautifulSoup
import requests
import json


def headlinegrabber(response_text):
    soup = BeautifulSoup(response_text, 'lxml')
    headlines = soup.find_all(attrs={"id": "initialStateDom"})
    for headline in headlines:
        print(headline.text)



url = 'https://www.cbc.ca/news'
response = requests.get(url)
headlinegrabber(response.text)