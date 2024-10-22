from bs4 import BeautifulSoup
import os.path
from os.path import expanduser
import requests

def get_ul(url: str):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup.find('ul')

def get_today_events(url: str, file_dir: str):
    ul_soup = get_ul(url)
    for li in ul_soup.find_all('li'):
        write_file(li.text, file_dir)

def write_file(li: str, file_dir: str):
    with open(file_dir, 'a') as f:
        f.write(li)
        f.write('\n')

home = expanduser("~")
home_dir = os.path.join(home, 'taran-luca-on-this-day/on_this_day.txt')
get_today_events('https://en.wikipedia.org/wiki/Wikipedia:On_this_day/Today', home_dir)