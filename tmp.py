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