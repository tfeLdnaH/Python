#count a specific word
import requests
from bs4 import BeautifulSoup
import operator

def start(url):
    word_list = []
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code)
    for post_text in soup.findAll('a', {'class':'singleListingTitles'}): #get link which is = "a", grab "class", where  class = 'singleListingTitles'
        content = post_text.string #only get the text, not html
        words = content.lower().split() #separete in words lower case
        for each_word in words:
            #print(each_word)
            word_list.append(each_word)
    clean_up_list(word_list)

def clean_up_list(word_list):
    clean_word_list = []
    for word in word_list:
        symbols = "!@#$%¨&*()-_+="
        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], "")
        if len(word) > 0:
            #print(word)
            clean_word_list.append(word)
    create_dictionary(clean_word_list)


def create_dictionary(clean_word_list):
    word_count = {}
    for word in clean_word_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    for key, value in sorted(word_count.items(), key=operator.itemgetter(1))#itemgetter(1) = value or itemgetter(0) = key
        print(key, value)

start('http://buckysroom.org/tops.php?type=text&period=this-month')
