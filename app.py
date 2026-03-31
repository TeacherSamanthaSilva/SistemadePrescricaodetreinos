from flask import Flask, request, jsonify
from workout_generator import generate_workout
from exercises_db import exercises

app = Flask(__name__)

@app.route("/")
def home():
    return "API de Treino de Calistenia rodando 🚀"

@app.route("/generate", methods=["POST"])
def generate():
    user = request.json

    required_fields = ["level", "goal", "days_per_week", "equipment"]
    for field in required_fields:
        if field not in user:
            return jsonify({"error": f"Campo obrigatório: {field}"}), 400

    workout = generate_workout(user, exercises)

    return jsonify({
        "user": user,
        "plan": workout
    })

if __name__ == "__main__":
    app.run(debug=True)