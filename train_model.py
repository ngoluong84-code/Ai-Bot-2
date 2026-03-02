import pandas as pd
import numpy as np
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Đọc dữ liệu
df = pd.read_csv("btc_1h_with_indicators.csv")

# Tạo target: giá tăng >2% sau 72 giờ (3 ngày)
future_shift = 72
df["future_return"] = df["close"].shift(-future_shift) / df["close"] - 1
df["target"] = (df["future_return"] > 0.02).astype(int)

# Xóa dòng NaN
df = df.dropna()

# Chọn feature
features = ["ema20", "ema50", "rsi14", "volume"]
X = df[features]
y = df["target"]

# Chia train/test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, shuffle=False
)

# Train model
model = XGBClassifier()
model.fit(X_train, y_train)

# Đánh giá
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print("Model Accuracy:", accuracy)

# Lưu model
model.save_model("btc_model.json")

print("Model đã lưu thành công")