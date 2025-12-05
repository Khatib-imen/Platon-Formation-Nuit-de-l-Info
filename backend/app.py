from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from crawler_client import crawl_website  # ton scraper existant
from bs4 import BeautifulSoup

app = Flask(__name__, static_folder="../frontend")
CORS(app)

@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")

@app.route("/<path:filename>")
def static_files(filename):
    return send_from_directory(app.static_folder, filename)

@app.route("/scrape", methods=["POST"])
def scrape():
    data = request.json
    url = data.get("url", "")

    if not url.startswith(("http://", "https://")):
        return jsonify({"error": "URL invalide"}), 400

    try:
        result = crawl_website(url)
        html = result.get("html", "")
        result["cleaned_html"] = html  # Pour afficher directement dans iframe
        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)
