#http://openweathermap.org/api

import requests
#import json
from pprint import pprint
def main():
    response = requests.get("http://samples.openweathermap.org/data/2.5/forecast?q=M%C3%BCnchen,DE&appid=b1b15e88fa797225412429c1c50c122a1")
    weather = response.json()
    #pprint(weather)
    #print(weather)
    pprint(weather)

if __name__ == '__main__':
    main()
    
