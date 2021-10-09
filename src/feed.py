import requests
from .url import *


class Feed :

    def __init__(self, url):
        self.url = url + '/rss'
        self.response = requests.get(self.url)

        if(int(self.getResponseStatus()) == 200):
            print("it works")
            print(self.response.content)

    def getURL(self):
        return self.url

    def getResponseFull(self):
        return self.response

    def getResponseStatus(self):
        return self.response.status_code

    def getResponseContent(self):
        return self.response.content
