#encoding: utf-8
import re
import string
allStrings = ['Did Angelina Jolie Want To Marry Colin Farrell And Settle For Brad Pitt Instead?','Epic A Cappella Cover Of Taylor Swift\'s "I Knew You Were Trouble"','Pennsylvania Governor Sues NCAA Over Penn State Sanctions','A "Les Miz" Character Guide','Probably The Most Amazing Cover Photo Album On Facebook','Chris Christie Shames Congress, Boehner For Sandy Relief Delay','Anthony Bourdain Live-Tweeted An Episode Of iCarly','16 Songs That Are Now 50 Years Old','The Most Mind-Shattering Defensive Football Play Of The Year','First Out LGBT Person Elected To Pennsylvania Legislature Sworn In','Supercut: Every Stan Lee Marvel Movie Cameo Ever','The Best Misheard Song Lyrics From 2012','Very Detailed Summary Of "Les Miserables"']

phrases = re.compile(r".*")


for s in allStrings:
	if s[len(s)-1] not in string.punctuation:
		s = s + '.'
	print re.findall("\\b(?:(?<=\")[^\"]*(?=\")|.?)",s)
	

