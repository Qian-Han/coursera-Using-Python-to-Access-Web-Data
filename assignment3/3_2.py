import urllib
from bs4 import BeautifulSoup

url = raw_input('Enter - ')
count = int(raw_input('Enter count: '))
position = int(raw_input('Enter position: '))
for i in range(count+1):
	html = urllib.urlopen(url).read()
	soup = BeautifulSoup(html, 'html.parser')
	# Retrieve all of the anchor tags
	tags = soup.find_all('a')
	print "Retrieving: ", url
	tag = tags[position-1]
	url = tag.get('href', None)