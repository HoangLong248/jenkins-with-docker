from flask import Flask

app = Flask(__name__)

@app.route("/hello")
def home():
	return "Hello World!"

app.run(host="0.0.0.0")
