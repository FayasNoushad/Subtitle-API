# Made with python3
# (C) @FayasNoushad
# Copyright permission under MIT License
# All rights reserved by FayasNoushad
# License -> https://github.com/FayasNoushad/Subtitle-API/blob/main/LICENSE

from flask import Flask, redirect, request, jsonify, json


app = Flask(__name__)


@app.route("/")
def home():
    return "Documentation:- <a href='https://github.com/FayasNoushad/Subtitle-API'>Subtitle-API</a>"


@app.route("/results/", methods=['GET'])
def subtitle_results():
    query = request.args.get('query')
    dict_result = results(query)
    if results is not None:
        return jsonify(dict_result)


if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=5000, use_reloader=True, threaded=True)
