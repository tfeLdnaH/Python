#dont allow the google crawler some file
import urllib.request #for request to my url, download file from internet
import io

def get_robots_txt(url):
    if url.endswith('/'):
        path = url
    else:
        path = url + '/'
    req = urllib.request.urlopen(path + "robots.txt", data=None)
    data = io.TextIOWrapper(req, encoding='utf-8')
    return data.read()

print(get_robots_txt('https://reddit.com/'))


