#encoding: utf-8
import random
import re
import bfUtils
import articleGenerator


def getFirstWord(fileName):
	words = fileName.read().split()
	return words[random.randint(0, len(words)-1)]

def findLines(firstWord,fileName):
	output = []
	for line in fileName.readlines():
		tokenizedLine = bfUtils.tokenizeLine(line)
		if len(tokenizedLine) > 0:
			if firstWord == tokenizedLine[0]:
				output.append(line)
	return output

def generateHeadline(firstWordsFile, allArticles, markovGenerator):
	lines = []
	for line in allArticles.readlines():
		lines.append(line.split(' ')[0])
	count = 0
	while count < 10:
		allArticles.seek(0)
		firstWordsFile.seek(0)
		firstWord = getFirstWord(firstWordsFile)
		randomLine = random.choice(findLines(firstWord,allArticles))
		secondWord = bfUtils.tokenizeLine(randomLine)[1]
		
		candidate =  markovGenerator.generate_markov_text(firstWord,secondWord)
		if (bfUtils.validSentence(candidate,lines)):
			return candidate
		count = count + 1

if __name__ == "__main__":
	firstWordsFile = open('firstWords.txt')
	allArticles = open('bfArticles-cleaned.txt')
	m = articleGenerator.Markov(allArticles)

	for i in range (0,10):
		print generateHeadline(firstWordsFile,allArticles,m)