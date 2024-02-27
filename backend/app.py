# This is just some random generated boilerplate code to have something initial
from flask import Flask, request, jsonify
from flask_cors import CORS
import string
app = Flask(__name__)
CORS(app)


def rev_str(s: str) -> str:
    """This is a sample util to demonstrate how to do unit testing in tests/unit/test_utils.py"""
    return s[::-1]

def sent_analysis(s: str) -> dict:
    # Function to clean and split words from the input string
    def clean_and_split(word):
        cleaned_word = word.lower().strip(string.punctuation)
        return cleaned_word, word

    # Split the input string using spaces
    words = s.split()

    # Clean and split each word using predefined symbols
    cleaned_words_with_punctuation = [clean_and_split(word) for word in words]

    marked_words = {
        'love': {'score': 0.8, 'color': 'rgb(163 230 53)'},
        'sunny': {'score': 0.9, 'color': 'rgb(132 204 22)'},
        'days': {'score': 0.1, 'color': 'rgb(77 124 15)'},
        'but': {'score': -.1, 'color': 'rgb(202 138 4)'},
        'hate': {'score': -.9, 'color': 'rgb(244 63 94)'},
        'rain': {'score': -.1, 'color': 'rgb(120 53 15)'},
    }

    sentiment_score = round(sum(marked_words.get(word[0], {}).get('score', 0) for word in cleaned_words_with_punctuation), 3)

    # Mark words with colors, using the original word for display
    marked_string = ' '.join(
        [f'<span style="background-color: {marked_words[word[0]]["color"]}">{word[1]}</span>'
        if word[0] in marked_words else word[1] for word in cleaned_words_with_punctuation])

    return marked_string, sentiment_score


@app.route("/reverse_string", methods=["POST"])
def reverse_string():
    data = request.json
    string_to_reverse = data.get("string", "")
    reversed_string = rev_str(string_to_reverse)
    return jsonify({"reversed_string": reversed_string})


@app.route("/api/v1/authorship/writeprint", methods=["POST"])
def generate_writeprint():
    return request.json


@app.route("/api/v1/authorship/writeprint/<job_id>", methods=["GET"])
def get_writeprint_results(job_id):
    return jsonify({"job_id": job_id})


@app.route("/api/v1/text/rephrase", methods=["POST"])
def rephrase():
    return request.json


@app.route("/api/v1/text/obfuscate", methods=["POST"])
def obfuscate():
    return request.json


@app.route("/api/v1/text/sentiment-analysis", methods=["POST"])
def sentiment_analysis():
    data = request.json
    string_to_mark = data.get("string", "")
    words, score = sent_analysis(string_to_mark)
    return jsonify({"words": words, "score": score})


@app.route("/api/v1/text/predict-user-attributes", methods=["POST"])
def predict_user_attributes():
    return request.json


@app.route("/api/v1/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy"})


if __name__ == "__main__":
    app.run(debug=True)
