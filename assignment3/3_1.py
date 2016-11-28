import urllib
import re
from bs4 import BeautifulSoup

html = urllib.urlopen('http://python-data.dr-chuck.net/comments_339284.html').read()

soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('td')

total = 0
for tag in tags:
	# Look at the parts of a tag
	line = str(tag)
	x = re.findall('[0-9]+',line)
	if len(x) > 0:
		for item in x:
			total += int(item)

print(total)