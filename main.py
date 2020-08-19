from urllib.request import urlopen
import re
from bs4 import BeautifulSoup

url = 'https://trainpix.org/update.php?time=24'
# url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)

# получение неформатированного html (class 'bytes')
html = page.read()

# преообразование html в str (читаемый вид)
html_decode = html.decode("utf-8")
print(html_decode)
# name_pos = html_decode.find('Name:')
# name_end = html_decode.find('</h2>')
# color_pos = html_decode.find('Favorite Color:')
# color_end = html_decode.find('</center>')

# создаем объект bs4
soup = BeautifulSoup(html_decode, 'html.parser')

# только текст без тегов
text_only = soup.get_text()

# любое упомниане
img = soup.find_all('img')

# получить аттрибуты
for i in img:
	print(i)
	link_s = str('https://trainpix.org'+i['src'])
	link_dwnld = link_s.replace('_s','')
	print(link_dwnld)

# содержимое тега
# title = soup.title.string
# print(title)

# создаем регулярку для любого написания тега title и содержимого его
# pattern = '<title.*?>.*?</title.*?>'
# match = re.search(pattern, html_decode, re.IGNORECASE)

# преобразуем полученный объект class re.Match в str
# title_old = match.group()

# с помощью регулярки удаляем все лишние символы
# title_new = re.sub('<.*?>', '', title_old)

# print(html_decode)
# print(html_decode[name_pos:name_end])
# print(html_decode[color_pos:color_end])
