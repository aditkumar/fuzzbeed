import articleGenerator
import bfeed
import bfHeadline
import json

from flask import Flask, render_template
app = Flask(__name__)
app.debug = True
secret = json.loads(open('./apis.txt').read())
# apikey = secret.get('tumblrAPI')
giphyAPIkey = secret.get('giphyAPI')

firstWordsFile = open('./firstWords.txt')
allArticles = open('./bfArticles-cleaned.txt')
validWords = json.loads(open('allNouns.txt').read()).keys()
m = articleGenerator.Markov(allArticles, validWords)

@app.route("/")
def homepage():
	headlinePhrase = bfHeadline.generateHeadline(firstWordsFile,allArticles,m)
	keywords = headlinePhrase[1]
	title = headlinePhrase[0]
	tumblrData = []
	for keyword in keywords:
		tumblrData.extend(bfeed.getGiphyData(giphyAPIkey, keyword))
	# return json.dumps(postData, indent=1)
	return render_template('layout.html', headline=title, postData=tumblrData[:4])

if __name__ == "__main__":
    app.debug = True
    app.run()
