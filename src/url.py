import requests
import re as parser

#
def validateURL(url):
    splitURL = parser.split('/|\.', url)

    containsRSS = False

    for item in splitURL:
        if(item == 'rss'):
            containsRSS = True

    if(containsRSS):

        response = requests.get(url)

        if(int(response.status_code) == 200):
            print(response.text[2:5])

