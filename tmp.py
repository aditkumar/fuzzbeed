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


allWords = json.loads(open('wordFreq.json').read())
allNouns = {}
for word in allWords.keys():
	if nltk.pos_tag([word.lower()])[0][1][0] == 'N' and allWords[word] > 20:
		allNouns[word] =  allWords[word]
f = open('allNouns.txt','w')
f.write(json.dumps(allNouns,indent=1))
f.close()