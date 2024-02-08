# This is just some random generated boilerplate code to have something initial
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


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
    return request.json


@app.route("/api/v1/text/obfuscate", methods=["POST"])
def obfuscate():
    return request.json


@app.route("/api/v1/text/sentiment-analysis", methods=["POST"])
def sentiment_analysis():
    return request.json


@app.route("/api/v1/text/predict-user-attributes", methods=["POST"])
def predict_user_attributes():
    return request.json


@app.route("/api/v1/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy"})


if __name__ == "__main__":
    app.run(debug=True)
