from flask import Flask, request, jsonify

app = Flask(__name__)

multipliers = []

@app.route('/')
def home():
    return "server ok"

@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    if not data or "value" not in data:
        return jsonify({"error": "bad request"}), 400

    value = float(data["value"])
    multipliers.append(value)

    return jsonify({"status": "added"})

@app.route('/predict')
def predict():
    if len(multipliers) == 0:
        return jsonify({"prediction": 1.0})

    avg = sum(multipliers) / len(multipliers)
    return jsonify({"prediction": round(avg, 2)})
