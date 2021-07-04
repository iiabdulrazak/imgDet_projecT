from bs4 import BeautifulSoup as bs
import requests as req
import re
import urllib.request
import os

def get_soup(url):
    return bs(req.get(url).text, 'html.parser')

image_type = "games"
query = "games"
url = "http://www.bing.com/images/search?q=" + query + "&qft=+filterui:color2-bw+filterui:imagesize-large&FORM=R5IR3"

soup = get_soup(url)
images = [a['src'] for a in soup.find_all("img", {"src": re.compile("mm.bing.net")})]

for img in images:
    raw_img = urllib.request.urlopen(img).read()
    save_loc = '../testing/img/'
    if not os.path.exists(save_loc):
        os.mkdir(save_loc)
    cntr = len([i for i in os.listdir(save_loc) if image_type in i])
    f = open(save_loc + image_type + str(cntr), 'wb')
    f.write(raw_img)
    f.close()