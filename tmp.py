#encoding: utf-8
import re
import string
import nltk
import csv

import articleGenerator
import bfUtils
import bfHeadline

fileName = open('sentenceStructures-withFrequencies')

lines = []
for line in fileName.readlines():
	lines.append(line.split(' ')[0])

s = '18 Cute Cozies Your Tortoise Can Rock Winter'
print bfUtils.validSentence(s,lines)


# firstWordsFile = open('firstWords.txt')
# allArticles = open('bfArticles-cleaned.txt')
# m = articleGenerator.Markov(allArticles)

# for i in range (0,3):
# 	headline = bfHeadline.generateHeadline(firstWordsFile,allArticles,m)
# 	tokens = nltk.word_tokenize(headline)
# 	tagged = nltk.pos_tag(tokens)
# 	print tagged


# lines = allArticles.readlines()
# out = open('sentenceStructures-withFrequencies','w')
# cw = csv.writer(out, delimiter='\n')
# lineStructures = {}
# count = 1
# for line in lines:
	# print nltk.sent_tokenize(line)
	# print nltk.word_tokenize(line)
	
# 	print bfUtils.sentenceStructure(line)

# 	if count % 100 == 0:
# 		print count
# 	if count > 100:
# 		break
# 	count = count + 1

# toAdd = []
# for k in sorted(lineStructures, key=lineStructures.get , reverse=True):
# 	toAdd.append(''.join( [k , ' ' , str(lineStructures.get(k))] ))

# cw.writerows([toAdd])
# out.close()
	# print k , lineStructures.get(k)
# 	out.writelines(k , lineStructures.get(k))
	
	# print pos_tags
	# print text
	



'''
tagged = nltk.FreqDist( tag for (word, tag) in out)
print tagged
for k in tagged.keys():
	print k , tagged[k]
'''