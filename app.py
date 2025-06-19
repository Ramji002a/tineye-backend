
from flask import Flask, request, jsonify
from flask_cors import CORS  # ✅ Added for CORS support
import requests

app = Flask(__name__)
CORS(app)  # ✅ Enable CORS for all routes

@app.route("/search", methods=["POST"])
def search():
    data = request.get_json()
    image_url = data.get("url")

    if not image_url:
        return jsonify({"error": "No URL provided"}), 400

    # Simulated response structure (since TinEye API keys are sensitive)
    # Replace this section with actual API call logic if you have access
    dummy_response = {
        "results": {
            "matches": [
                {
                    "domain": "example.com",
                    "backlinks": ["https://example.com/image-match"],
                    "score": 99.5
                },
                {
                    "domain": "sample.net",
                    "backlinks": ["https://sample.net/image"],
                    "score": 88.2
                }
            ]
        }
    }

    return jsonify(dummy_response)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
