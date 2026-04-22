from flask import Flask, request, jsonify

app = Flask(__name__)

data = []

@app.route('/')
def home():
    return "API OK"

@app.route('/send', methods=['POST'])
def send():
    value = float(request.json.get("value"))
    data.append(value)
    return jsonify({"status": "added"})

@app.route('/predict', methods=['GET'])
def predict():
    if len(data) == 0:
        return jsonify({"prediction": 2.0})

    avg = sum(data) / len(data)
    last = data[-5:]
    low = len([x for x in last if x < 2])

    if low >= 3:
        pred = 4.0
    elif avg > 3:
        pred = 2.0
    else:
        pred = 3.0

    return jsonify({"prediction": pred})