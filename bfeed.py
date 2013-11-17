#encoding: utf-8
import urllib2
import requests
import re
from datetime import date
from datetime import timedelta
from bs4 import BeautifulSoup
import articleGenerator

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

def getTumblrData(api_key, tag):
	payload = {'tag' : tag ,'api_key' : api_key}
	tumblrTags = 'http://api.tumblr.com/v2/tagged'
	r = requests.get(tumblrTags, params=payload)

	output = []
	for post in r.json()['response']:
		outpost = {}
		outpost['source'] = post['short_url']
		if 'title' in post.keys() and 'body' in post.keys():
			outpost['title'] = post['title']
			body = post['body']
			imgs = re.findall('"http.+["$]',body)
			if len(imgs) > 0:
				outpost['img'] = imgs[0].strip('"')
		if 'photos' in post.keys():
			for photo in post['photos']:
				outpost['title'] = ''.join( BeautifulSoup( post.get('caption') ).findAll( text = True ) )
				outpost['img']  = photo.get('original_size').get('url')
		output.append(outpost)
	return output
	
def tokenizeLine(s):
	tokens = re.findall("(?:(?<=[\"])[^\"]*(?=[\"]*)|[\\w\'()?\n]+)",s)
	if len(tokens) == 0:
		return []
	if tokens[len(tokens)-1] == '\n':
		tokens.pop()
		if len(tokens) == 0:
			return []
		tokens[len(tokens)-1] = tokens[len(tokens)-1] + '\n'
	return tokens

def sentenceStructure(line):
	tagged =  nltk.pos_tag(tokenizeLine(line.lower()))
	structure = ''.join([part[1] for part in tagged])
	return structure

def validSentence(s,validStructures):
	ss = sentenceStructure(s)
	print (ss)
	return validStructures.count(ss) > 0 

def countFirstWords(filename):
	words = {}
	for line in filename.readlines():
		lineWords = tokenizeLine(line)
		if len(lineWords) > 0:
			first = lineWords[0]
			if first not in words:
				words[first] = 1
			else:
				words[first] = words.get(first) + 1
	return words

def countWords(filename):
	words = {}
	for fline in filename.readlines():
		lineWords = tokenizeLine(fline)
		for word in lineWords:
			if word not in words:
				words[word] = 1
			else:
				words[word] = words.get(word) + 1
	return words

def countConditionalLines(lines):
	words = {}
	for line in lines:
		word = line.split(' ')[0]
		if word not in words:
			words[word] = 1
		else:
			words[word] = words.get(word) + 1
	return words

def questionLines(filename):
	for line in filename.readlines():
		if line[len(line)-2] == "?":
			yield line

def generateWordFrequency(allArticles):
	words  = []
	allArticles.seek(0)
	for line in allArticles.readlines():
		linewords = tokenizeLine(line.strip('\n').lower())
		words.extend(linewords)
	fdist = nltk.FreqDist(words)
	f = open('wordFreq.json','w')
	f.write(json.dumps(fdist,indent=2))
	f.close()