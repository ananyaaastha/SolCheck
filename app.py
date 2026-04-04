from flask import Flask, render_template, request, jsonify
from auditor import audit_contract
import traceback

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/audit", methods=["POST"])
def audit():
    data = request.get_json()
    code = data.get("code", "").strip()

    if not code:
        return jsonify({"error": "No contract code provided."}), 400

    if len(code) > 50_000:
        return jsonify({"error": "Contract too large. Max 50,000 characters."}), 400

    try:
        result = audit_contract(code)
        return jsonify(result)
    except Exception as e:
        traceback.print_exc()
        return jsonify({"error": f"Audit failed: {str(e)}"}), 500


if __name__ == "__main__":
    app.run(debug=True, port=5000)
