import requests
#way to requst informantio from internet
from bs4 import BeautifulSoup

def trade_spider(max_pages):
    page = 1
    while page <= max_pages
        url = 'http://buckysroom.org/trade/search;php?page=' + str(page)
        source_code = requests.get(url) #get all source code from the url
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text) #all data here
        for link in soup.findAll('a', {'class':'item-name'}): # a href, get all link from the source page which is a list of book for example
            href = "http://buckysroom.org/" + link.get('href') #example of return for each link that find on the webpage url
                                                               # -> http://buckysroom.org/trade/view.php?id=64
            title = link.string#called string the name of container of the "item-name" from webpage url
            print(href)
            print(title)
        page += 1


trade_spider(1)

