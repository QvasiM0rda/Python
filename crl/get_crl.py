'''Скрипт для скачивания списков отозванных сертификатов (СОС) с сайтов ФНС и Казначейства,
потому что они обновляются каждый день и я устал качать их ручками'''

import os, wget, requests  # os - для взаимодействия с файловой системой; wget скачивает файл; requests получает get-запрос из url
from bs4 import BeautifulSoup as bs  # BeautifulSoup нужен для парсинга get-запроса и получения из него ссылок    

os.chdir('p:/!Admin/CRL')  # Каталог, куда будут скачиваться СОС

# Список адресов, где лежат СОС
url_list = ['http://10.200.0.100/crl', 'http://10.200.0.100/cdp', 'http://crl.roskazna.ru/crl/', 'http://reestr-pki.ru/cdp/']
request_list = [requests.get(url) for url in url_list]
soups = [bs(request.text, 'html.parser') for request in request_list]

# Получаем ссылки из get-запросов
links = []

for soup in soups:
    for link in soup.find_all('a'):
        link = link.get('href')
        if link[-3:] != 'crl':  # Отсеиваем сертификаты и другие ссылки по расширению
            continue

        # Для СОС на сайте ФНС ссылки начинаются с /. На сайте казны они либо лежат в той же директории, либо на другом сайте,
        # откуда скачать их можно, только имею прямую ссылку.
        if link[0] == '/':
            link = 'http://10.200.0.100' + link
        elif link[0:4] != 'http':
            link = 'http://crl.roskazna.ru/crl/' + link
        links.append(link)

# links - список всех полученных ссылок на СОС
for link in links:
    filename = wget.filename_from_url(link)
    if os.path.exists(filename):
        os.remove(filename)
    try:
        wget.download(link)
    except:
        print('The link is broken')
