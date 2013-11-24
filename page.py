import articleGenerator
import bfeed
import bfHeadline
import json

from flask import Flask, render_template
app = Flask(__name__)
secret = json.loads(open( os.path.join(os.path.dirname(__file__), './secret.json')).read())
apikey = secret.get('tumblrAPI')

firstWordsFile = open( os.path.join(os.path.dirname(__file__), './firstWords.txt'))
allArticles = open( os.path.join(os.path.dirname(__file__), './bfArticles-cleaned.txt'))
m = articleGenerator.Markov(allArticles)

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