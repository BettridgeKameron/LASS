# This is just some random generated boilerplate code to have something initial
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/reverse_string', methods=['POST'])
def reverse_string():
    data = request.json
    string_to_reverse = data.get('string', '')
    reversed_string = string_to_reverse[::-1]
    return jsonify({'reversed_string': reversed_string})

if __name__ == '__main__':
    app.run(debug=True)

