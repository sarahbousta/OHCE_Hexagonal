from flask import Flask, request, jsonify
from flask_cors import CORS
from ohce import Ohce

app = Flask(__name__)
CORS(app)

@app.route('/greet')
def api_greet():
    language = request.args.get('lang', default='fr')
    ohce = Ohce(language=language)
    return jsonify(greeting=ohce.greet())

@app.route('/echo', methods=['POST'])
def api_echo():
    data = request.json
    text = data.get('text', '')
    ohce = Ohce()
    return jsonify(echo=ohce.echo(text))

@app.route('/farewell')
def api_farewell():
    language = request.args.get('lang', default='fr')
    ohce = Ohce(language=language)
    return jsonify(farewell=ohce.farewell())