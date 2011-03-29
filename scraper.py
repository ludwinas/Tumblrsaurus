#scraper.py
import math
import string
from lxml import etree
import urllib2
import time, random

username = "crendice"
iURL = "http://"+username+".tumblr.com/api/read/"
URL = ""
urlList = []
step = 20
#GLOBAL
maxIterations = 0
currentIteration = 0

def fetch(url):
	try:
		request = urllib2.Request(url)
		request.add_header("User-Agent", "Mozilla/5.0 (X11; U; Linux x86_64; fr; rv:1.9.1.5) Gecko/20091109 Ubuntu/9.10 (karmic) Firefox/3.5.5")
		return urllib2.urlopen(request).read()
	except IOError:
		print "Ooops"

def getTotal():
	global maxIterations
	XML = fetch(iURL)
	root = etree.fromstring(XML)
	total = root.find("posts").attrib['total']
	maxIterations = math.floor(int(total)/step)
	maxIterations = int(maxIterations)
	print total

def iterationCheck():
	global currentIteration
	if currentIteration < maxIterations:
		print "di"
		num = str(step*currentIteration)
		URL = iURL+"?start="+num
#		print URL
		iterate(URL)
	else:
		print "job finished"

def iterate(URL):
	global currentIteration
	time.sleep(random.randint(1,3))
	XML = fetch(URL)
	root = etree.fromstring(XML)
	for post in root.iterfind(".//post"):
		urlList.append(post.attrib['url'])
	print urlList
	currentIteration+=1
	iterationCheck()

getTotal()
iterationCheck()




