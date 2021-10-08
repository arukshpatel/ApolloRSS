import requests
import re as parser

def validateURL(url):

    slashSplit = parser.split('/|\.', url)
    containsRSS = False

    for item in slashSplit:
        if(item == 'rss'):
            containsRSS = True
            print(item)

    if(containsRSS):
        print("true")
