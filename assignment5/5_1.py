import urllib
import json

serviceurl = raw_input('Enter URL: ')
uh = urllib.urlopen(serviceurl)
data = uh.read()
try: js = json.loads(str(data))
except: js = None
comments = js['comments']
total = 0
for comment in comments:
	total += comment['count']
print total