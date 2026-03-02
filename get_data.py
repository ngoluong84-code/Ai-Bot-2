from binance.client import Client
import pandas as pd

# Không cần API key để lấy dữ liệu public
client = Client()

# Lấy dữ liệu BTCUSDT khung 1 giờ (1h)
klines = client.get_historical_klines(
    "BTCUSDT",
    Client.KLINE_INTERVAL_1HOUR,
    "1 Jan, 2023"
)

# Chuyển thành DataFrame
df = pd.DataFrame(klines, columns=[
    "time", "open", "high", "low", "close", "volume",
    "close_time", "qav", "num_trades",
    "taker_base_vol", "taker_quote_vol", "ignore"
])

# Chỉ giữ các cột quan trọng
df = df[["time", "open", "high", "low", "close", "volume"]]

# Chuyển time sang dạng datetime
df["time"] = pd.to_datetime(df["time"], unit="ms")

# Chuyển dữ liệu sang số
for col in ["open", "high", "low", "close", "volume"]:
    df[col] = df[col].astype(float)

# Lưu thành file CSV
df.to_csv("btc_1h.csv", index=False)

print("Đã lưu dữ liệu vào btc_1h.csv")