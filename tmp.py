#encoding: utf-8
import re
import string

f = open('bfArticles-cleaned.txt')
allStrings = f.readlines()

count = 0
for s in allStrings:
	print re.findall("(?:(?<=[\"])[^\"]*(?=[\"]*)|[\\w\'()?\n]+)",s)
	
	count = count + 1
	if (count > 1000):
		break
	
# # Clean up quotation marks
# f  = open('bfArticles.txt')
# f2 = open('bfArticles-cleaned.txt','w')
# for line in f.readlines():
# 	line = line.replace('“','"').replace('”','"').replace('’','\'')
# 	f2.writelines(line)
# f2.close
