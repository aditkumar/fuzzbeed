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


# 	print ("http://www.buzzfeed.com/archive/" + single_date.strftime("%Y/%m/%d"))
# currentURL = 'http://www.buzzfeed.com/archive/2013/11/13'
# page = urllib2.urlopen(currentURL).read()
# soup = BeautifulSoup(page)
# soup.prettify()
# for article in soup.find_all("li",class_="bf_dom"):
# 	print article.find('a').text.encode('utf-8').strip()
	
output = open('bfArticles.txt', 'w')
for single_date in dateRange( date(2013,1,1), date(2013,11,15) ):
	print(single_date)
	writeDay(single_date, output)
output.close()


# f = open('bfArticles-cleaned.txt')

# # words = countWords(f)
# # for w in sorted(words, key=words.get,reverse=True):
# # 	if(words.get(w) < 20):
# # 		break
# # 	if(w.find(' ') > 0):
# # 		print(w, words.get(w))

# # words = countWords(f)
# # for w in sorted( words , key=words.get, reverse=True):
# # 	if (words.get(w) < 100):
# # 		break
# # 	print(w , words.get(w))

# # Output first words to file
# words = countFirstWords(f)
# output = open('firstWords.txt','w')
# for word in sorted(words , key=words.get, reverse=True):
# 	if ( words.get(word) < 100 ):
# 		break
# 	output.write(word +'\n')
# output.close()