#encoding: utf-8
import urllib2
from datetime import date
from datetime import timedelta
from bs4 import BeautifulSoup

def dateRange(start_date , end_date):
	for n in range(int ((end_date - start_date).days)):
		yield start_date + timedelta(n)

def writeDay( day, file):
	currentURL = 'http://www.buzzfeed.com/archive/' + day.strftime("%Y/%m/%d")
	page = urllib2.urlopen(currentURL).read()
	soup = BeautifulSoup(page)
	soup.prettify()
	for article in soup.find_all("li",class_="bf_dom"):
		aTitle = article.find('a').text.encode('utf-8').strip()
		if len(aTitle) > 0 :
			file.write(aTitle + "\n")

def pullArticles():
	output = open('bfArticles.txt', 'w')
	for single_date in dateRange( date(2013,1,1), date(2013,11,15) ):
		print(single_date)
		writeDay(single_date, output)
	output.close()

def cleanInputFile():
	# Clean up quotation marks
	f  = open('bfArticles.txt')
	f2 = open('bfArticles-cleaned.txt','w')
	for line in f.readlines():
		line = line.replace('“','"').replace('”','"').replace('’','\'')
		f2.writelines(line)
	f2.close()
	f1.close()


def createFirstWordFile():
	# Output first words to file
	words = countFirstWords(f)
	output = open('firstWords.txt','w')
	for word in sorted(words , key=words.get, reverse=True):
		if ( words.get(word) < 100 ):
			break
		output.write(word +'\n')
	output.close()