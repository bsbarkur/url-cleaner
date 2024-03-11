from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/clean')
def about():
    url = request.args.get('url')
    return jsonify({"cleaned_url": url})
