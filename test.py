import urllib2, urlparse, html5lib, lxml
from lxml.cssselect import CSSSelector

#global
notes = '/notes/4063336729/IacUx21it?from_c='

base = 'http://ludwinas.tumblr.com'
target = base + notes
usernames = []


def showmoreNotes():
# try to open URL ...
	try:
		global target
		request = urllib2.Request(target)
		request.add_header("User-Agent", "Mozilla/5.0 (X11; U; Linux x86_64; fr; rv:1.9.1.5) Gecko/20091109 Ubuntu/9.10 (karmic) Firefox/3.5.5")
		f=urllib2.urlopen(request)

		# Is it really something that I can parse? srsly?
		try:
			parser = html5lib.HTMLParser(tree=html5lib.treebuilders.getTreeBuilder("lxml"), namespaceHTMLElements=False)
			page = parser.parse(f)
		except ValueError, err:
			print "Value Error:", err, target

		if CSSSelector('a.more_notes_link[onclick]')(page): # Any links for me?
			global notes
			global usernames
			#getting the 'show more notes' link
			for link in CSSSelector('a.more_notes_link[onclick]')(page):
				onclick = urlparse.urljoin(f.geturl(), link.attrib['onclick'])
				mySubString=onclick[onclick.find("GET','")+6:onclick.find("',true")]
				
				#----getting the reblogs and putting them in a list----
				#if CSSSelector('li.note like a[href]')(page): # Any links for me?
				for link in CSSSelector('li.note a[href]')(page):
					href = urlparse.urljoin(f.geturl(), link.attrib['href'])
					usernames.append(href)
#					if not link.text in ['None', 'Show more notes'] and link.attrib['title'] == 'View Post':
#						usernames.append(href)
					usernames = list(set(usernames))
					b = open("usernames.html", "a")
					b.write(str(usernames))
					b.close()
					#print >>b, usernames
					#print usernames
				
				#----end of getting rebloggers part----
				
				
				#repeating the function to go to another page with notes
				b = open("usernames.html", "a")
				b.write(mySubString)
				#print >>b, mySubString
				b.close()
				notes = mySubString
				target = base + notes
				showmoreNotes()
		else:
			print "finished"

	# ... catch HTTP and URL errors
	except urllib2.HTTPError, err:
		print "HTTP Error:",err.code , target
		print "trying other URL"
	except urllib2.URLError, err:
		print "URL Error:",err.reason , target
		print
		
showmoreNotes()
