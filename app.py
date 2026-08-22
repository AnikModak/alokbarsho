"""
app.py
Entry point for the Lunar Image Registration web app (SIH PS 26166).

Run with: python app.py
"""

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    return "Lunar Image Registration — placeholder. Build the UI here."


@app.route("/register", methods=["POST"])
def register():
    # TODO: wire up src/registration.py pipeline here
    return jsonify({"status": "not_implemented"})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
