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
		return post
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

if __name__ == "__main__":
	print json.dumps(getTumblrData('p8HvsZZVGCX5NsbdwKeVMBVa8QMDm095lYr2CiiPTuNza5tIZq','art'),indent=1)


'''
for post in postData:
	if 'img' not in post.keys():
		continue

'''



# wfreq = open('wordFreq.json')
# wfreqdict = json.loads(wfreq.read())
# # for word in bfeed.tokenizeLine(headline):
# 	print word, wfreqdict.get(word.lower()), nltk.pos_tag([word.lower()])[0][1]





# tag = 'kobe dunk'
# tposts = bfeed.getTumblrData(apikey,tag)
# print json.dumps(tposts,indent=2)