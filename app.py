from flask import Flask, render_template
import random
app=Flask(__name__)
#list of cat images
Images=[https://scratchpads.eu/explore/sites-list]
@app.route(‘/’)
Def index():
url = random.choice(images)
return render_template(‘index.html’,url=url)
if __name__ == “__main__”:
	app.run(host=”0.0.0.0”)
