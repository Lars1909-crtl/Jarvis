from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
load_dotenv()
import brain
import wishlist as wishlist_mod

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    text = data.get("text", "").strip()
    if not text:
        return jsonify({"answer": "Ich habe dich nicht verstanden. Sag es nochmal?"})
    answer = brain.handle_command(text)
    return jsonify({"answer": answer})

@app.route("/wishlist", methods=["GET"])
def get_wishlist():
    return jsonify(wishlist_mod.get_all())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
