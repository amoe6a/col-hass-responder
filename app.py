from flask import Flask, jsonify
import requests

app = Flask(__name__)

data = requests.get('https://colonist.io/api/game-list').json()

@app.route('/')
def get_data():
    resp = jsonify(data)
    resp.headers['Access-Control-Allow-Origin'] = '*'  # Allow all origins
    return resp

if __name__ == '__main__':
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
