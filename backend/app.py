from flask import Flask, request, jsonify
from flask_cors import CORS
import html
import random  # Rephrase

# Sentiment Analysis
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Rephrase
from parrot import Parrot
from nltk.tokenize import sent_tokenize
import warnings

warnings.filterwarnings("ignore")

app = Flask(__name__)
app.json.sort_keys = False
CORS(app)

nltk.download("vader_lexicon", quiet=True)  # Sentiment Analysis
parrot = Parrot(model_tag="prithivida/parrot_paraphraser_on_T5")  # Rephrase
nltk.download("punkt")  # Rephrase


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


def rephrase_sentence(sentence: str) -> str:
    """
    Attempt to rephrase a sentence using Parrot; return the original sentence if it's too long or an error occurs.
    """
    tokens = nltk.word_tokenize(sentence)
    if len(tokens) <= 32:
        try:
            paraphrases = parrot.augment(
                input_phrase=sentence, use_gpu=False, do_diverse=True
            )
            return paraphrases[0][0] if paraphrases else sentence
        except Exception as e:
            print(f"Error rephrasing sentence: {e}")
            return sentence
    return sentence


@app.route("/api/v1/text/rephrase", methods=["POST"])
def rephrase():
    # TODO: There are a many issues with this, but this could be fixed probably once
    #       we use a completely different approach. Again, for now this is a placeholder
    #       that "works" and should be heavily modified in the future, as we are not
    #       trying to make this a paraphraser, but a rephraser.
    data = request.json
    text_to_rephrase = data.get("text", "")
    if not text_to_rephrase:
        return jsonify({"error": "No text provided"}), 400

    sentences = sent_tokenize(text_to_rephrase)
    rephrased_sentences = []

    for sentence in sentences:
        rephrased_sentence = rephrase_sentence(sentence)
        if sentence[0].isupper():
            rephrased_sentence = rephrased_sentence[0].upper() + rephrased_sentence[1:]
        rephrased_sentences.append(rephrased_sentence)

    rephrased_text = " ".join(rephrased_sentences)
    if not rephrased_text:
        return jsonify({"error": "Failed to generate a rephrase"}), 500

    return jsonify({"rephrased_result": rephrased_text})


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
