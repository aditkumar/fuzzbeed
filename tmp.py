# encoding: utf-8
from bs4 import BeautifulSoup
import re
import string
import nltk
import csv

import json 
import articleGenerator
import bfUtils
import bfeed
import bfHeadline

# def getTumblrData(api_key, tag):
# 	payload = {'tag' : tag ,'api_key' : api_key}
# 	tumblrTags = 'http://api.tumblr.com/v2/tagged'

# 	r = requests.get(tumblrTags, params=payload)


# 	output = []
# 	for post in r.json()['response']:
# 		outpost = {}
# 		# print json.dumps(post, indent=2)
# 		outpost['source'] = post['short_url']
# 		if 'title' in post.keys():
# 			outpost['title'] = post['title']
# 			body = post['body']
# 			outpost['img'] = re.findall('"http.+["$]',body)[0].strip('"')
# 		if 'photos' in post.keys():
# 			for photo in post['photos']:
# 				outpost['title'] = ''.join( BeautifulSoup( post.get('caption') ).findAll( text = True ) )
# 				outpost['img']  = photo.get('original_size').get('url')
# 		output.append(outpost)
# 	return output

apikey = 'p8HvsZZVGCX5NsbdwKeVMBVa8QMDm095lYr2CiiPTuNza5tIZq'
tag = 'kobe dunk'
tposts = bfeed.getTumblrData(apikey,tag)
print json.dumps(tposts,indent=2)