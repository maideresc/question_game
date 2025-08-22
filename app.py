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
    "Who painted The Last Supper?",
    "What is the longest river in the world?",
    "Which planet is known as the Red Planet?",
    "Who wrote Romeo and Juliet?",
    "What is the smallest prime number?",
    "Which country hosted the 2016 Summer Olympics?",
    "Who discovered penicillin?",
    "What is the hardest natural substance on Earth?",
    "Which organ in the human body pumps blood?",
    "What is the largest ocean on Earth?",
    "Who was the first person to walk on the Moon?",
    "What is the main language spoken in Brazil?",
    "Which continent is the Sahara Desert located in?",
    "Who invented the telephone?",
    "What is the boiling point of water in Celsius?",
    "Which famous scientist formulated the laws of motion?"
]

# Ruta principal que carga la página de inicio (index.html)
@app.route("/")
def index():
    return render_template("index.html")

# Ruta que devuelve una pregunta al azar
@app.route("/question")
def get_question():
    return jsonify({"question": random.choice(questions)})

if __name__ == "__main__":
    app.run(debug=True)


