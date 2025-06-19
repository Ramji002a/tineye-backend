from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# ✅ आपकी TinEye API Keys
API_AUTH = ("LCkn,2K7osVwkX95K4Oy", "6mm60lsCNIB,FwOWjJqA80QZHh9BMwc-ber4u=t^")
TINEYE_API_URL = "https://api.tineye.com/rest/search/"

@app.route("/search", methods=["POST"])
def search_image():
    data = request.json
    image_url = data.get("url")

    if not image_url:
        return jsonify({"error": "Missing image URL"}), 400

    payload = {
        "image_url": image_url,
        "offset": 0,
        "limit": 10,
        "sort": "score",
        "order": "desc"
    }

    try:
        response = requests.post(TINEYE_API_URL, data=payload, auth=API_AUTH)
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
