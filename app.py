from flask import Flask, render_template, jsonify, request
import pandas as pd
from xgboost import XGBClassifier
import subprocess
from flask import jsonify, request
// sửa ở đây//
app = Flask(__name__)

MODEL_PATH = "btc_model.json"

def load_model():
    model = XGBClassifier()
    model.load_model(MODEL_PATH)
    return model

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict")
def predict():
    tf = request.args.get("tf", "1h")

    from predict import get_prediction
    probability, signal = get_prediction(tf)

    return jsonify({
        "probability": probability,
        "signal": signal
    })

@app.route("/train", methods=["POST"])
def train():
    subprocess.run(["python", "train_model.py"])
    return jsonify({"status": "Model retrained successfully"})

if __name__ == "__main__":
    app.run(debug=True)
