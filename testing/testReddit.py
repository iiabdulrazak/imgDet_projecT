try:
	import os
	import json
	import requests as req
	from bs4 import BeautifulSoup as bs
except Exception as e:
	print(f"error while importing packages!\n\n{e}")

GOOGLE_IMAGE = \
    'https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990&'

usr_agent = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive',
}

def main():
	#create folder to save images
	save_loc = 'img'
	if not os.path.exists(save_loc):
		os.mkdir(save_loc)
	download_img()

def download_img():
	data = input("enter type of search: ")
	num_img = int(input("number of images you need: "))

	print("start searching ...")

	search_link = GOOGLE_IMAGE + 'q=' + data
	print(f"Link to the Images: {search_link}")

	res = req.get(search_link, headers=usr_agent)
	webDetails = res.text
	soup = bs(webDetails, 'html.parser')
	results = soup.find_all('div',{'class':'rg_i'})
	print(results)

main()