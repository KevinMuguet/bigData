from flask import Flask, render_template, url_for, json, jsonify, request
import os
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello world !"
	
@app.route('/books')
def books():
	SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
	json_url = os.path.join(SITE_ROOT, '', 'books.json')
	data = json.load(open(json_url))
	return jsonify(data)
	
@app.route('/books/<book_name>')
def book(book_name):
	SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
	json_url = os.path.join(SITE_ROOT, '', 'books.json')
	data = json.load(open(json_url))
	for row in data:
		for attribute, value in row.items():
			if(attribute == "title" and value==book_name):
				return row

if __name__ == "__main__":
    app.run()