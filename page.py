import articleGenerator
import bfeed
import bfHeadline
import json

from flask import Flask, render_template
app = Flask(__name__)

firstWordsFile = open('./firstWords.txt')
allArticles = open('./bfArticles-cleaned.txt')
m = articleGenerator.Markov(allArticles)
secret = json.loads(open('./apis.txt').read())
apikey = secret.get('tumblrAPI')



@app.route("/")
def homepage():
	headlinePhrase = bfHeadline.generateHeadline(firstWordsFile,allArticles,m)
	keyword = headlinePhrase[1]
	title = headlinePhrase[0]
	tumblrData = bfeed.getTumblrData(apikey, keyword)
	postData = []
	for post in tumblrData:
		if 'img' not in post.keys():
			continue
		postData.append(post)
	# return json.dumps(postData, indent=1)
	return render_template('layout.html', headline=title, postData=postData)

if __name__ == "__main__":
    app.debug = True
    app.run()