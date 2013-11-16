import random
import articleGenerator

def getFirstWord(fileName):
	import random
	words = fileName.read().split()
	return words[random.randint(0, len(words)-1)]

def findLines(firstWord,fileName):
	output = []
	for line in fileName.read().split("\n"):
		if firstWord in line.split(' ')[0]:
			output.append(line)
	return output

firstWords = open('firstWords.txt')
firstWord = getFirstWord(firstWords)
allArticles = open('bfArticles.txt')
randomLine = random.choice(findLines(firstWord,allArticles))
secondWord = randomLine.split(' ')[1]

m = articleGenerator.Markov(allArticles)
print m.generate_markov_text(firstWord,secondWord)