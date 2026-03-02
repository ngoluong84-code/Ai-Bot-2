import pandas as pd
import ta

# Đọc dữ liệu
df = pd.read_csv("btc_1h.csv")

# Tính EMA20 và EMA50
df["ema20"] = ta.trend.ema_indicator(df["close"], window=20)
df["ema50"] = ta.trend.ema_indicator(df["close"], window=50)

# Tính RSI14
df["rsi14"] = ta.momentum.rsi(df["close"], window=14)

# Lưu file mới
df.to_csv("btc_1h_with_indicators.csv", index=False)

print("Đã thêm EMA & RSI vào dữ liệu")