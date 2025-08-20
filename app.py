# file: app.py
from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

# List of questions
questions = [
    "What is the capital of France?",
    "Who was the first President of the United States?",
    "In what year did World War II start?",
    "Which civilization built the pyramids of Egypt?",
    "Who developed the theory of relativity?",
    "Which chemical element has the symbol O?",
    "Which gas do we need to breathe?",
    "What is the process by which plants make their food called?",
    "Which is the largest planet in the solar system?",
    "Who painted The Last Supper?"
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/question")
def get_question():
    return jsonify({"question": random.choice(questions)})

if __name__ == "__main__":
    app.run(debug=True)
