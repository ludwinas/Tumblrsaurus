#scraper.py
import math
import string
from lxml import etree

iURL = "http://ludwinas.tumblr.com/api/read/"
URL = ""
urlList = []
current = 0
step = 20
currentIteration = 0
#GLOBAL
maxIterations = 0


def getTotal():
	global maxIterations
	root = etree.parse(iURL).getroot()
	total = root.find("posts").attrib['total']
	maxIterations = math.floor(int(total)/step)
	maxIterations = int(maxIterations)

getTotal()

def iterate(URL):
	root = etree.parse(URL).getroot()
	for post in root.iterfind(".//post"):
		urlList.append(post.attrib['url'])
	currentIteration+1

#current = len(urlList)
print currentIteration
print maxIterations

print currentIteration < maxIterations

if currentIteration < maxIterations:
	print "di"
	num = str(step*currentIteration)
	URL = iURL+"?start="+num
	print URL
#	iterate(URL)

