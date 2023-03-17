from flask import Flask, jsonify, request
import random
import string

app = Flask(__name__)

urls = {}

@app.route('/shorten', methods=['POST'])
def shorten():
    url = request.json['url']
    short_id = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
    short_url = request.host_url + short_id
    urls[short_id] = url
    return jsonify({'short_url': short_url})

@app.route('/<short_id>')
def redirect_to_url(short_id):
    if short_id not in urls:
        return jsonify({'error': 'Invalid short URL'}), 404
    return jsonify({'url': urls[short_id]})

if __name__ == '__main__':
    app.run(debug=True)
