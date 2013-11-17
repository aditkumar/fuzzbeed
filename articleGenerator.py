#encoding: utf-8
import random
import string 
import re
import bfeed
import nltk
import json

class Markov(object):
	# Adapted from code from Shabda Raaj found at: http://agiliq.com/blog/2009/06/generating-pseudo-random-text-with-markov-chains-u/
	def __init__(self, open_file):
		self.cache = {}
		self.open_file = open_file
		self.words = self.file_to_words()
		self.word_size = len(self.words)
		self.database()
		
	
	def file_to_words(self):
		wordList = list()
		self.open_file.seek(0)
		for line in self.open_file.readlines():
			tokenizedLine = bfeed.tokenizeLine(line)
			wordList.extend(tokenizedLine)
		return wordList
		
	
	def triples(self):
		""" Generates triples from the given data string. So if our string were
				"What a lovely day", we'd generate (What, a, lovely) and then
				(a, lovely, day).
		"""
		
		if len(self.words) < 3:
			return
		
		for i in range(len(self.words) - 2):
			yield (self.words[i], self.words[i+1], self.words[i+2])
			
	def database(self):
		for w1, w2, w3 in self.triples():
			key = (w1, w2)
			if key in self.cache:
				self.cache[key].append(w3)
			else:
				self.cache[key] = [w3]
				
	def generate_markov_text(self, firstWord, secondWord, size=11):
		wfreq = open('wordFreq.json')
		wfreqdict = json.loads(wfreq.read())
		w1, w2 = firstWord , secondWord
		gen_words = [w1,w2]
		while len ( re.findall('\n',w2) ) < 1 and len(gen_words) < 30:
			w1, w2 = w2, random.choice(self.cache[(w1, w2)])
			gen_words.append(w2)
		keyword = w2.lower().strip('\n')
		for word in gen_words:
			pos = nltk.pos_tag([word.lower()])[0][1]
			freq = wfreqdict.get(word.lower().strip('\n'))
			if pos[0] == 'N'  and freq > 10 and freq > wfreqdict.get(keyword):
				keyword = word.lower().strip('\n')
		wfreq.close()
		return [' '.join(gen_words).strip('\n') , keyword]
			
			
		