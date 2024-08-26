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
    app.run(debug=True)
