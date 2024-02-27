# This is just some random generated boilerplate code to have something initial
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


def rev_str(s: str) -> str:
    """This is a sample util to demonstrate how to do unit testing in tests/unit/test_utils.py"""
    return s[::-1]

#Code block below marks the words "the"
#------------------------
def sent_analysis(s: str) -> list:
    words = s.split()
    sentiment_score = 0
    marked_string = ' '.join([f'<span style="background-color: #66ff00; ">{word}</span>' if word.lower() == 'the' else word for word in words])
    sentiment_score += round(0.8 * s.lower().count('the'), 3)

    print(sentiment_score)
    return marked_string, sentiment_score

#------------------------

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
