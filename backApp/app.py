from flask import Flask, jsonify
import requests
from waitress import serve

app = Flask(__name__)

@app.route('/')
def get_data():
    data = requests.get('https://colonist.io/api/game-list').json()
    resp = jsonify(data)
    resp.headers['Access-Control-Allow-Origin'] = '*'  # Allow all origins
    return resp

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8080)
