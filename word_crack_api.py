# Words API for a fun word game
# Author: Jacob Atkinson

from flask import Flask, jsonify, request, send_from_directory
import random

app = Flask(__name__)

def get_dictionary():
    """
    Get the wordlist from the file words.txt and read it into a list.
    """

    words = []
    f = open("./words.txt")
    for line in f:
        words.append(line.strip())
    f.close()
    return words

@app.route("/api/new_word", methods=["GET"])
def get_word():
    dictionary = get_dictionary()
    word = ""

    while len(word) < 6:
        word = random.choice(dictionary)
    return jsonify(word)

@app.route("/api/check_word", methods=["GET"])
def check_word():
    dictionary = get_dictionary()
    response = False
    word = request.args.get('word', '')
    if word in dictionary:
        response = True
    return {"data": {"word": word, "is_word": response}}

@app.route("/")
def svelte_app():
    return send_from_directory("word_crack/public", "index.html")

@app.route("/<path:path>")
def home(path):
    return send_from_directory("word_crack/public", path)
