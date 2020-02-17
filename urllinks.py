import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter - ')
#count = 0
count = int(input('Enter count: '))
position = int(input('Enter position: '))
val = position
print('Retrieving:', url)
while count > 0:
    position = 0
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    for tag in tags:
        position, tag.get('href', None)
        position += 1
        if position == val:
            url = tag.get('href', None)
            print('Retrieving: ', url)
            break
    count -= 1
