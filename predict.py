import os
import json
import random
import numpy as np


MODEL_PATH = "btc_model.json"


def load_model():
    """
    Load model nếu tồn tại.
    Nếu không có thì trả về None.
    """
    if os.path.exists(MODEL_PATH):
        with open(MODEL_PATH, "r") as f:
            model = json.load(f)
        return model
    return None


def fake_feature_engineering(tf):
    """
    Tạo feature giả lập theo timeframe.
    Sau này bạn có thể thay bằng indicator thật.
    """
    if tf == "1h":
        base = 0.5
    elif tf == "4h":
        base = 0.55
    elif tf == "1d":
        base = 0.6
    else:
        base = 0.5

    noise = random.uniform(-0.2, 0.2)
    return base + noise


def model_predict(model, feature_value):
    """
    Dự đoán bằng model đơn giản.
    Model ở đây giả lập logistic weight.
    """
    weight = model.get("weight", 1.0)
    bias = model.get("bias", 0.0)

    z = weight * feature_value + bias
    probability = 1 / (1 + np.exp(-z))
    return float(probability)


def get_prediction(tf="1h"):
    """
    Hàm chính được Flask gọi.
    Luôn trả về:
        probability (float)
        signal (LONG / SHORT)
    """

    model = load_model()

    feature_value = fake_feature_engineering(tf)

    if model:
        probability = model_predict(model, feature_value)
    else:
        # Nếu chưa train model
        probability = random.random()

    signal = "LONG" if probability > 0.5 else "SHORT"

    return probability, signal