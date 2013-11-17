#encoding: utf-8
import random
import re
import csv
import bfeed
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
	allArticles.seek(0)
	firstWordsFile.seek(0)
	firstWord = getFirstWord(firstWordsFile)
	randomLine = random.choice(findLines(firstWord,allArticles))
	secondWord = bfUtils.tokenizeLine(randomLine)[1]
	
	candidate =  markovGenerator.generate_markov_text(firstWord,secondWord)
	return candidate
	
if __name__ == "__main__":
	firstWordsFile = open('firstWords.txt')
	allArticles = open('bfArticles-cleaned.txt')
	m = articleGenerator.Markov(allArticles)

	out = open('sampleHeadlines.txt','w')
	cw = csv.writer(out, delimiter='\n')
	outList = []
	for i in range (0,100):
		outList.append(generateHeadline(firstWordsFile,allArticles,m).strip())
	
	cw.writerows([outList])
	out.close()
	firstWordsFile.close()
	allArticles.close()