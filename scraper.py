#scraper.py
import math
import string
from lxml import etree
import urllib2
import time, random

username = "ludwinas"
iURL = "http://"+username+".tumblr.com/api/read/"
URL = ""
step = 20
#GLOBAL
urlList = []
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
	global urlList
	if currentIteration < maxIterations:
		print currentIteration
		num = str(step*currentIteration)
		URL = iURL+"?start="+num
#		print URL
		iterate(URL)
	else:
		print "job finished"
		print urlList

def iterate(URL):
	global currentIteration
	global urlList
	time.sleep(random.randint(1,3))
	XML = fetch(URL)
	root = etree.fromstring(XML)
	for post in root.iterfind(".//post"):
		if post.attrib['type']=='photo':
			urlList.append(post.attrib['url'])
			
		else:
			print "no photo here"
		#THIS IS the loop that fetches the post url
		#we can also get other informations about it (like the post type)
	currentIteration+=1
	iterationCheck()

getTotal()
iterationCheck()
