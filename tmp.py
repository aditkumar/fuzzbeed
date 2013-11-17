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

secret = json.loads(open('secret.json').read())
apikey = secret.get('tumblrAPI')
print apikey
tag = 'kobe dunk'
tposts = bfeed.getTumblrData(apikey,tag)
print json.dumps(tposts,indent=2)