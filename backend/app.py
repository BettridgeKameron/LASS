# This is just some random generated boilerplate code to have something initial
from flask import Flask, request, jsonify
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from flask_cors import CORS
import html

app = Flask(__name__)
app.json.sort_keys = False
CORS(app)
nltk.download("vader_lexicon", quiet=False)


def rev_str(s: str) -> str:
    """This is a sample util to demonstrate how to do unit testing in tests/unit/test_utils.py"""
    return s[::-1]


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
    data = request.json
    string_to_rephrase = data.get("text", "")
    rephrased_string = rev_str(string_to_rephrase)
    return jsonify({"rephrased_result": rephrased_string})


@app.route("/api/v1/text/obfuscate", methods=["POST"])
def obfuscate():
    return request.json

def analyze_sentiment(text):
    sia = SentimentIntensityAnalyzer()
    sentiment = sia.polarity_scores(text)
    overall_score = ((sentiment["compound"] + 1) / 2) * 100

    words = text.split()
    words_sentiments = []
    for word in words:
        word_score = sia.polarity_scores(word)["compound"]
        encoded_word = html.escape(word)  # XSS Mitigation
        words_sentiments.append({encoded_word: word_score})

    return {
        "sentimentResults": {
            "score": f"{overall_score:.1f}",
            "words": words_sentiments,
        }
    }

@app.route("/api/v1/text/sentiment-analysis", methods=["POST"])
def sentiment_analysis():
    data = request.get_json()
    text = data.get("text", "")
    if not text:
        return jsonify({"error": "No text provided"}), 400

    results = analyze_sentiment(text)
    return jsonify(results)

@app.route("/api/v1/text/predict-user-attributes", methods=["POST"])
def predict_user_attributes():
    return request.json


@app.route("/api/v1/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy"})


if __name__ == "__main__":
    app.run(debug=True)
