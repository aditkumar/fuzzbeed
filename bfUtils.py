#encoding: utf-8
import articleGenerator
import re

def tokenizeLine(s):
	tokens = re.findall("(?:(?<=[\"])[^\"]*(?=[\"]*)|[\\w\'()?\n]+)",s)
	if len(tokens) == 0:
		return []
	if tokens[len(tokens)-1] == '\n':
		tokens.pop()
		if len(tokens) == 0:
			return []
		tokens[len(tokens)-1] = tokens[len(tokens)-1] + '\n'
	return tokens

def countFirstWords(filename):
	words = {}
	for line in filename.readlines():
		lineWords = tokenizeLine(line)
		if len(lineWords) > 0:
			first = lineWords[0]
			if first not in words:
				words[first] = 1
			else:
				words[first] = words.get(first) + 1
	return words

def countWords(filename):
	words = {}
	for fline in filename.readlines():
		lineWords = tokenizeLine(fline)
		for word in lineWords:
			if word not in words:
				words[word] = 1
			else:
				words[word] = words.get(word) + 1
	return words

def countConditionalLines(lines):
	words = {}
	for line in lines:
		word = line.split(' ')[0]
		if word not in words:
			words[word] = 1
		else:
			words[word] = words.get(word) + 1
	return words

def questionLines(filename):
	for line in filename.readlines():
		if line[len(line)-2] == "?":
			yield line