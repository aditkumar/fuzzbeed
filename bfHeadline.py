#encoding: utf-8
import random
import re
import firstWords
import articleGenerator


def getFirstWord(fileName):
	words = fileName.read().split()
	return words[random.randint(0, len(words)-1)]

def findLines(firstWord,fileName):
	output = []
	for line in fileName.readlines():
		tokenizedLine = firstWords.tokenizeLine(line)
		if len(tokenizedLine) > 0:
			if firstWord == tokenizedLine[0]:
				output.append(line)
	return output


firstWordsFile = open('firstWords.txt')
firstWord = getFirstWord(firstWordsFile)



allArticles = open('bfArticles-cleaned.txt')
randomLine = random.choice(findLines(firstWord,allArticles))
secondWord = firstWords.tokenizeLine(randomLine)[1]

m = articleGenerator.Markov(allArticles)
print m.generate_markov_text(firstWord,secondWord)