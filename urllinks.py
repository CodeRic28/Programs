# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

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
print('Blastoff!')
'''
# Retrieve all of the anchor tags
count = 0
pos = 0
tags = soup('a')
for tag in tags:
    pos = pos + 1
    print(pos, tag.get('href', None))
    if pos == 3:
        sp_one = tag.get('href', None).split('_')
        sp_two = sp_one[2].split('.')
        name = sp_two[0]
        nurl = 'http://py4e-data.dr-chuck.net/known_by_'+name+'.html'
        print('Retrieving: ', nurl)
        html = urllib.request.urlopen(nurl).read()
        soup = BeautifulSoup(html, 'html.parser')
        tags = soup('a')
        count = count + 1
        pos = 0

print(count)
'''
