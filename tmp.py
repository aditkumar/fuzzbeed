# encoding: utf-8
from bs4 import BeautifulSoup
import re
import string
import nltk
import csv
import json 
import articleGenerator
import bfeed
import bfHeadline
import random
import requests
from flask import Flask

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
		if 'img' in outpost.keys():
			output.append(outpost)
	return output

def getGiphyData(api_key, headline):
	payload = {'q' : headline ,'api_key' : api_key}
	giphySearch = 'http://api.giphy.com/v1/gifs/search'
	r = requests.get(giphySearch, params=payload)

	output =[]
	for post in r.json()['data']:
		currentpost = {}
		currentpost['source'] = post['embed_url']
		currentpost['img'] = post['images']['original']['url']
		output.append(currentpost)
	return json.dumps(output, indent=1)


secret = json.loads(open('./apis.txt').read())
apikey = secret.get('tumblrAPI')
giphyAPIkey = 'dc6zaTOxFJmzC'

firstWordsFile = open('./firstWords.txt')
allArticles = open('./bfArticles-cleaned.txt')
m = articleGenerator.Markov(allArticles)

headline =  bfHeadline.generateHeadline(firstWordsFile,allArticles,m)
output = []
print headline
print getGiphyData(giphyAPIkey, headline[1])

'''
for keyword in headline[1]:
	output.append(bfeed.getTumblrData(apikey,keyword))
print json.dumps(output, indent=1)
'''