from flask import Flask, request, jsonify, render_template
from services.ai_service import analyze_code

app = Flask(__name__)

@app.route("/")
def home_route():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    question = data.get("question")
    code = data.get("code")

    result = analyze_code(question, code)
    return jsonify(result)

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000, debug = True)
