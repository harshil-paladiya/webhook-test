from flask import Flask, request, jsonify
import os

app = Flask(__name__)


@app.route('/test_endpoint', methods=['POST'])
def test_endpoint():
    request_payload = request.json  # Get the request payload
    return jsonify(request_payload)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
