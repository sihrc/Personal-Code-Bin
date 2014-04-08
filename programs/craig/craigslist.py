import smtplib, urllib2
import pickle as p
import os, random
from bs4 import BeautifulSoup as soup

username = "sihrc.c.lee@gmail.com"
password = "Cl120193"
body_of_email = [\
"Hi!<br><br>I'm wondering if a 3 month term from mid-May is possible?<br><br>%s<br><br>Thanks!",\
"Hello<br><br>Would a 3 month stay starting mid-May be possible for your listing?<br><br>%s<br><br>Thank you",\
"Hi,<br><br>Could I stay for a 3 month period over the summer (mid-May)<br><br>%s<br><br>Regards",\
"Hello!<br><br>I'm looking for a place to stay over the summer for 3 months. Would that be possible for your listing?<br><br>%s<br><br>Thank you!",\
"Hello,<br><br>Is it possible to stay at this listing for a 3 month period starting mid-May?<br><br>%s<br><br>Looking forward to hearing back!"\
]

def setup():
	session = smtplib.SMTP('smtp.gmail.com',587)
	session.ehlo()
	session.starttls()
	session.login(username, password)
	return session

def getRecipient(url):
	read = soup(urllib2.urlopen(url).read())
	read = soup(urllib2.urlopen("http://sfbay.craigslist.org%s" % read.find("span",{"class":"replylink"}).a['href']).read())
	return read.find("input", {"class":"anonemail"})['value']

def getUrls(url):
	read = soup(urllib2.urlopen(url).read())
	urls = list()
	for found in read.find_all("a", {"class":"i"}):
		urls.append("http://sfbay.craigslist.org%s" % found['href'])
		print "found", urls[-1]
	return urls

def filterUrls(prev, new):
	return list(set([url for url in new if url not in prev]))

def loadUrls():
	if not os.path.exists("urls.p"):
		return list()
	with open("urls.p", 'rb') as f:
		return p.load(f)

def saveUrls(urls):
	with open("urls.p",'wb') as f:
		p.dump(urls,f)

if __name__ == "__main__":
	session = setup()
	prevUrls = loadUrls()
	low = 2000
	high = 5000
	mainUrl = "http://sfbay.craigslist.org/search/hhh/sfc?zoomToPosting=&catAbb=hhh&query=&minAsk=%d&maxAsk=%d&bedrooms=2&housing_type=&nh=1&excats=40" % (low,high)
	urls = getUrls(mainUrl)
	filtered_urls = filterUrls(prevUrls, urls)
	try:
		for url in filtered_urls:
			try:
				recipient = getRecipient(url)
			except:
				print "failed, %s" % recipient
				pass

			print "sent", recipient
			headers = "\r\n".join(["from: " + username, "subject: Listing",  "to: " + recipient, "mime-version: 1.0", "content-type: text/html"])
			content = headers + "\r\n\r\n" + random.choice(body_of_email) % url
			session.sendmail(username, recipient, content)
		saveUrls(set(list(urls) + list(filtered_urls) + list(prevUrls)))
	except:
		saveUrls(set(list(urls) + list(filtered_urls) + list(prevUrls)))
		
