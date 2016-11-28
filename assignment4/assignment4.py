import urllib
import xml.etree.ElementTree as ET

# Read in XML from the URL
url = raw_input('Enter url: ')
print 'Retrieving', url
xml = urllib.urlopen(url)
data = xml.read()

# Convert the XML to a tree
tree = ET.fromstring(data)

# Print how many characters in the XML
print 'Retrieved',len(data),'characters'

# Get all of the count values
tags = tree.findall('.//count')

# Total all of the counts
total = 0
for tag in tags:
    total += int(tag.text)

print total