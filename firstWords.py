import articleGenerator
import re
# m = articleGenerator.Markov(f)
# print m.generate_markov_text(10)
def tokenizeLine(s):
	tokens = re.findall("\\b(?:(?<=\")[^\"]*(?=\")|\\w+)\\b", s)
	return tokens

def countFirstWords(filename):
	words = {}
	for line in filename.readlines():
		lineWords = tokenizeLine(line)
		if len(lineWords) > 0:
			if first not in words:
				words[first] = 1
			else:
				words[first] = words.get(first) + 1
	return words

def countWords(filename):
	words = {}
	for word in tokenizeLine(filename.read()):
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

f = open('bfArticles.txt')
words = countWords(f)
for w in sorted(words, key=words.get,reverse=True):
	if(words.get(w) < 20):
		break
	if(w.find(' ') > 0):
		print(w, words.get(w))

# words = countWords(f)
# for w in sorted( words , key=words.get, reverse=True):
# 	if (words.get(w) < 100):
# 		break
# 	print(w , words.get(w))

# # Output first words to file
# words = countWords(f)
# output = open('firstWords.txt','w')
# for word in sorted(words , key=words.get, reverse=True):
# 	if ( words.get(word) < 100 ):
# 		break
# 	output.write(word+'\n')
# output.close()

