import wget
import requests
from bs4 import BeautifulSoup

url_crl = 'http://10.200.0.100/crl'
url_cdp = 'http://10.200.0.100/cdp'
url_kazna = 'http://crl.roskazna.ru/crl'
urls = []

reqs_crl = requests.get(url_crl)
reqs_cdp = requests.get(url_cdp)
reqs_kazna = requests.get(url_kazna)

soup_crl = BeautifulSoup(reqs_crl.text, 'html.parser')
soup_cdp = BeautifulSoup(reqs_cdp.text, 'html.parser')
soup_kazna = BeautifulSoup(reqs_kazna.text, 'html.parser')

#print("Getting links from", url_crl, end="... ")
#for link in soup_crl.find_all('a'):
 #   get_link = link.get('href')
  #  if len(get_link) > 1 and get_link[-1] == 'l' and get_link.find('%') == -1:
   #     urls.append('http://10.200.0.100' + get_link)
#print("Done!")

#print("Getting links from", url_cdp, end="... ")
#for link in soup_cdp.find_all('a'):
 #   get_link = link.get('href')
  #  if len(get_link) > 1 and get_link[-1] == 'l'  and get_link.find('%') == -1:
   #     urls.append('http://10.200.0.100' + get_link)
#print("Done!")

print("Getting links from", url_kazna, end="... ")
for link in soup_kazna.find_all('a'):
    get_link = link.get('href')
    if len(get_link) > 1 and get_link[-1] == 'l'  and get_link.find('%') == -1:
        if get_link[0] == 'h':
            urls.append(get_link)
        else:
            urls.append('http://crl.roskazna.ru/crl/' + get_link)
print("Done!")

for url in urls:
    print("Downloading: ", url, end="... ")
    file_name = 'd:/CRL/' + url[url.rfind('/') + 1::]
    wget.download(url, file_name)
    print("Done!")
