from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

def scrap_pic(url):
	page = urlopen(url)
	html = page.read()
	html_decode = html.decode("utf-8")
	soup = BeautifulSoup(html_decode, 'html.parser')
	text_only = soup.get_text()
	img = soup.find_all('img')
	for i in img:
		link_s = str('https://trainpix.org'+i['src'])
		link_dwnld = link_s.replace('_s','')
		name = link_s.replace('/', '').replace(':', '')
		if link_dwnld[-3::] == 'jpg':
			x = requests.get(link_dwnld)
			with open(f'h:/scrap/{name}.jpg', 'wb') as f:
				f.write(x.content)

scrap_pic('https://trainpix.org/update.php?time=36')
