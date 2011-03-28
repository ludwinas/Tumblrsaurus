#scraper.py

from lxml import etree

URL = "http://ludwinas.tumblr.com/api/read/"

tree = etree.parse(URL)
root = tree.getroot()

total = root.find("posts").attrib['total']

for post in root.iterfind(".//post"):
	print post.attrib['url']




